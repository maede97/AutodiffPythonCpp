from sympy import numbered_symbols, cse, ccode, Symbol, derive_by_array
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

def __sympyToC_Grad(exprs: list) -> str:
    """ creates C code from a list of sympy functions (somewhat optimized).

    source: https://stackoverflow.com/questions/22665990/optimize-code-generated-by-sympy
    and modified """

    tmpsyms = sympy.numbered_symbols("tmp")
    symbols, simple = sympy.cse(exprs, symbols=tmpsyms)
    c_code = ""
    for s in symbols:
        c_code +=  "  double " +sympy.ccode(s[0]) + " = " + sympy.ccode(s[1]) + ";\n"
    for i,s in enumerate(simple):
        c_code += f"  out({i}) = " + sympy.ccode(s) + ";\n"
    return c_code

def __sympyToC_Hess(exprs: list, num_der: int) -> str:
    """ creates C code from a list of sympy functions (somewhat optimized).
    Assumes that the output format is a hessian -> matrix.

    source: https://stackoverflow.com/questions/22665990/optimize-code-generated-by-sympy
    and modified """
    tmpsyms = sympy.numbered_symbols("tmp")
    symbols, simple = sympy.cse(exprs, symbols=tmpsyms)
    c_code = ""
    for s in symbols:
        c_code +=  "  double " +sympy.ccode(s[0]) + " = " + sympy.ccode(s[1]) + ";\n"
    for i in range(num_der):
        for j in range(num_der):
            if(i <= j):
                c_code += f"  out({i},{j}) = " + sympy.ccode(simple[i * num_der + j]) + ";\n"
            else:
                c_code += f"  out({i},{j}) = out({j}, {i});\n"
    return c_code

def __createParams(P: np.array, props: np.array):
    """ Creates a string with the parameters and properties accessed as they would be eigen vectors. """
    ret = ""
    for i in range(len(P)):
        ret += f"  const double P{i} = P({i});\n"
    for i in range(len(props)):
        ret += f"  const double props{i} = props({i});\n"
    return ret

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

    # master functions on top of header file
    final_header_code += f"void dDdP(const Eigen::Matrix<double,{len_P},1>& P, const Eigen::Matrix<double,{len_props},1>& props, Eigen::Matrix<double,{len_der},1>& out);\n"
    final_header_code += f"void d2DdP2(const Eigen::Matrix<double,{len_P},1>& P, const Eigen::Matrix<double,{len_props},1>& props, Eigen::Matrix<double,{len_der},{len_der}>& out);\n"
    
    final_header_code += "\n}" +f" /* namespace {namespace} */"

    # add c master function dDdP
    final_source_code += f"void dDdP(const Eigen::Matrix<double,{len_P},1>& P, const Eigen::Matrix<double,{len_props},1>& props, Eigen::Matrix<double,{len_der},1>& out) " + "{\n"
    final_source_code += __createParams(P, props)
    final_source_code += __sympyToC_Grad(list(derive_by_array(func, P[:len_der])))
    final_source_code += "}\n\n"

    final_source_code += f"void d2DdP2(const Eigen::Matrix<double,{len_P},1>& P, const Eigen::Matrix<double,{len_props},1>& props, Eigen::Matrix<double,{len_der},{len_der}>& out) " + "{\n"
    final_source_code += __createParams(P, props)
    first_der = derive_by_array(func, P[:len_der])
    second_der = derive_by_array(first_der, P[:len_der])
    # second_der is now a matrix -> flatten it
    exprs = []
    for row in second_der:
        for col in row:
            exprs.append(col)
    final_source_code += __sympyToC_Hess(exprs, len_der)
    
    final_source_code += "}\n"
    final_source_code += "\n}" +f" /* namespace {namespace} */"

    with open(filename + ".h", "w") as wr:
        wr.write(final_header_code)
    with open(filename + ".cpp", "w") as wr:
        wr.write(final_source_code)