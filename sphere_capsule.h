#pragma once

#include <Eigen/Core>

namespace CodeGen_SphereCapsule {

void dDdP(const Eigen::Matrix<double,9,1>& P, const Eigen::Matrix<double,2,1>& props, Eigen::Matrix<double,9,1>& dDdP_out);
void d2DdP2(const Eigen::Matrix<double,9,1>& P, const Eigen::Matrix<double,2,1>& props, Eigen::Matrix<double,9,9>& d2DdP2_out);

double dDdP_0(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double dDdP_1(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double dDdP_2(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double dDdP_3(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double dDdP_4(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double dDdP_5(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double dDdP_6(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double dDdP_7(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double dDdP_8(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);

double d2DdP2_0_0(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_0_1(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_0_2(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_0_3(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_0_4(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_0_5(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_0_6(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_0_7(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_0_8(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_1_1(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_1_2(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_1_3(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_1_4(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_1_5(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_1_6(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_1_7(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_1_8(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_2_2(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_2_3(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_2_4(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_2_5(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_2_6(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_2_7(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_2_8(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_3_3(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_3_4(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_3_5(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_3_6(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_3_7(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_3_8(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_4_4(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_4_5(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_4_6(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_4_7(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_4_8(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_5_5(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_5_6(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_5_7(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_5_8(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_6_6(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_6_7(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_6_8(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_7_7(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_7_8(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);
double d2DdP2_8_8(const double& P0, const double& P1, const double& P2, const double& P3, const double& P4, const double& P5, const double& P6, const double& P7, const double& P8, const double& props0, const double& props1);

} /* namespace CodeGen_SphereCapsule */