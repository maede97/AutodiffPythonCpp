import autodiffPythonCpp as apc
import sympy
import numpy as np

def sigmoid(x, scale, shift=0.5):
    return 1. / (1. + sympy.exp(-1. * scale * (x - shift)))

def compute_t(P):
    P0 = P[:3]
    P1 = P[3:6]
    P2 = P[6:9]
    t = -1 * (((P1-P0).dot(P2 - P1)) / apc.norm(P2 - P1) ** 2)
    return sigmoid(t, 5.) # sigScale

def computeClosestPointOnLine(P):
    P1 = P[3:6]
    P2 = P[6:9]
    return P1 + (P2 - P1) * compute_t(P)

def compute_D(P, props):
    P0 = P[:3]
    return apc.norm(P0 - computeClosestPointOnLine(P)) - props[0] - props[1]

# create a numpy array of symbols for both P and props
P = np.array(sympy.symbols('P:9'))
props = np.array(sympy.symbols('props:2'))
func = compute_D(P, props)

# call the generator
apc.create_header_source_files(func, P, props, 9, "sphere_capsule", "CodeGen_SphereCapsule")