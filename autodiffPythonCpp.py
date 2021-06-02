from sympy import numbered_symbols, cse, ccode, Symbol
import sympy
import typing
import numpy as np

def norm(v: np.array) -> sympy.Expr:
    """ Computes the norm of a vector. """
    l = len(v)
    sum_ = 0.
    for i in range(l):
        sum_ = sum_ + v[i] * v[i]
    return sympy.sqrt(sum_)

def __sympyToC(symfunc: sympy.Function) -> str:
    """ creates C code from a sympy function (somewhat optimized).

    source: https://stackoverflow.com/questions/22665990/optimize-code-generated-by-sympy
    and modified """


    tmpsyms = numbered_symbols("tmp")
    symbols, simple = cse(symfunc, symbols=tmpsyms)
    symbolslist = sorted(map(lambda x:str(x), list(symfunc.atoms(Symbol))))
    varstring=",".join( " double "+x for x in symbolslist )
    c_code = ""
    for s in symbols:
        c_code +=  "  double " +ccode(s[0]) + " = " + ccode(s[1]) + ";\n"
    c_code +=  "  double r = " + ccode(simple[0])+";\n"
    c_code +=  "  return r;\n"
    return c_code

def create_header_source_files(func : sympy.Function, P : np.array, props : np.array, num_derivatives : int, filename : str ="codegen", namespace : str ="Codegen") -> None:
    """ Create C code from a given function.
    @param func The function handle to take the first and second derivatives from.
    @param P The parameter vector
    @param props The properties vector
    @param num_derivatives How large the gradient and hessian are (gradient: num_derivatives x 1, hessian: num_derivatives x num_derivatives)
    @param filename Where to store the generated code
    @param namespace What namespace to put in
    """
    len_P = len(P)
    len_props = len(props)
    len_der = num_derivatives

    final_header_code = f"#pragma once\n\n#include <Eigen/Core>\n\nnamespace {namespace} "+"{\n\n"
    final_source_code = f"#include \"{filename}.h\"\n#include <cmath>\n\nusing namespace std;\n\nnamespace {namespace} "+"{\n\n"
    hessian_header_code = ""
    hessian_source_code = ""

    # master functions on top of header file
    final_header_code += f"void dDdP(const Eigen::Matrix<double,{len_P},1>& P, const Eigen::Matrix<double,{len_props},1>& props, Eigen::Matrix<double,{len_der},1>& dDdP_out);\n"
    final_header_code += f"void d2DdP2(const Eigen::Matrix<double,{len_P},1>& P, const Eigen::Matrix<double,{len_props},1>& props, Eigen::Matrix<double,{len_der},{len_der}>& d2DdP2_out);\n"
    final_header_code += "\n"

    header_arguments = ""
    for i in range(len_P):
        header_arguments += f"const double& P{i}, "
    for i in range(len_props-1):
        header_arguments += f"const double& props{i}, "
    header_arguments += f"const double& props{i+1}"
    arguments = ""
    for i in range(len_P):
        arguments += f"P({i}), "
    for i in range(len_props - 1):
        arguments += f"props({i}), "
    arguments += f"props({i+1})"

    for i in range(len_der):
        dDdPi = func.diff(P[i])

        final_header_code += f"double dDdP_{i}({header_arguments});\n"
        final_source_code += f"double dDdP_{i}({header_arguments}) "+"{\n"
        final_source_code += __sympyToC(dDdPi)
        final_source_code += "}\n"

        for j in range(len_der):
        # compute hessians
            if i <= j:
                hessianij = dDdPi.diff(P[j])
                hessian_header_code += f"double d2DdP2_{i}_{j}({header_arguments});\n"
                hessian_source_code += f"double d2DdP2_{i}_{j}({header_arguments}) "+"{\n"
                hessian_source_code += __sympyToC(hessianij)
                hessian_source_code += "}\n"

    # Add hessian source code
    final_header_code += f"\n{hessian_header_code}"
    final_source_code += f"\n{hessian_source_code}\n"
    
    final_header_code += "\n}" +f" /* namespace {namespace} */"

    # add c master function dDdP
    final_source_code += f"void dDdP(const Eigen::Matrix<double,{len_P},1>& P, const Eigen::Matrix<double,{len_props},1>& props, Eigen::Matrix<double,{len_der},1>& dDdP_out) " + "{\n"
    for i in range(len_der):
        final_source_code += f"    dDdP_out({i}) = dDdP_{i}({arguments});\n"
    final_source_code += "}\n"

    # add c master function d2DdP2
    final_source_code += f"void d2DdP2(const Eigen::Matrix<double,{len_P},1>& P, const Eigen::Matrix<double,{len_props},1>& props, Eigen::Matrix<double,{len_der},{len_der}>& d2DdP2_out) " + "{\n"
    for i in range(len_der):
        for j in range(len_der):
            #make use of the fact that the hessian is symmetric
            if i <= j:
                final_source_code += f"    d2DdP2_out({i},{j}) = d2DdP2_{i}_{j}({arguments});\n"
            else:
                final_source_code += f"    d2DdP2_out({i},{j}) = d2DdP2_out({j}, {i});\n"
    final_source_code += "}\n"
    # Add closing namespace
    final_source_code += "\n}" +f" /* namespace {namespace} */"

    with open(filename + ".h", "w") as wr:
        wr.write(final_header_code)
    with open(filename + ".cpp", "w") as wr:
        wr.write(final_source_code)