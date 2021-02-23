# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 00:38:28 2020

@author: SOFTECH
"""
#Author Oyero Abdullahi
import numpy as np
Y = 5.0
X = 5.0
#T2 = np.arctan2(Y,X)
T1 = 0
T2 = 0
T3 = 0
T4 = 0
T5 = 0 
T6 = 0
#link length
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
a7 = 0
#linear distance
d3 = 0 
#converting the angles to radian
T1 = (T1/180)*np.pi
T2 = (T2/180)*np.pi
T3 = (T3/180)*np.pi
T4 = (T4/180)*np.pi
T5 = (T5/180)*np.pi
T6 = (T6/180)*np.pi
#angle 90degrees in radian
Rad90= (90/180)*np.pi
#creating the dh parameter

dh       = [[      T1,       Rad90,     a2,      a1],
            [T2+Rad90,       Rad90,      0,       0],
            [       0,       Rad90,      0,a3+d3+a4],
            [       T4,     -Rad90,      0,      a5],
            [       T5,      Rad90,      0,       0],
            [       T6,          0,      0,   a6+a7]
           ]
# the homogenous transformation 
H0_1 = [
        [np.cos(dh[0][0]),-np.sin(dh[0][0])*np.cos(dh[0][1]), np.sin(dh[0][0])*np.sin(dh[0][1]), dh[0][2]*np.cos(dh[0][0])],
        [np.sin(dh[0][0]), np.cos(dh[0][0])*np.cos(dh[0][1]), -np.cos(dh[0][0])*np.sin(dh[0][1]), dh[0][2]*np.sin(dh[0][0])],
        [               0,                  np.sin(dh[0][1]),                   np.cos(dh[0][1]),                  dh[0][3]],
        [               0,                                 0,                                  0,                         1]
       ]
H1_2 = [
        [np.cos(dh[1][0]),-np.sin(dh[1][0])*np.cos(dh[1][1]), np.sin(dh[1][0])*np.sin(dh[1][1]), dh[1][2]*np.cos(dh[1][0])],
        [np.sin(dh[1][0]), np.cos(dh[1][0])*np.cos(dh[1][1]), -np.cos(dh[1][0])*np.sin(dh[1][1]), dh[1][2]*np.sin(dh[1][0])],
        [               0,                  np.sin(dh[1][1]),                   np.cos(dh[1][1]),                  dh[1][3]],
        [               0,                                 0,                                  0,                         1]
       ]
H2_3 = [
        [np.cos(dh[2][0]),-np.sin(dh[2][0])*np.cos(dh[2][1]), np.sin(dh[2][0])*np.sin(dh[2][1]), dh[2][2]*np.cos(dh[2][0])],
        [np.sin(dh[2][0]), np.cos(dh[2][0])*np.cos(dh[2][1]),-np.cos(dh[2][0])*np.sin(dh[2][1]), dh[2][2]*np.sin(dh[2][0])],
        [               0,                  np.sin(dh[2][1]),                   np.cos(dh[2][1]),                 dh[2][3]],
        [               0,                                 0,                                  0,                         1]
       ]
H3_4 = [
        [np.cos(dh[3][0]),-np.sin(dh[3][0])*np.cos(dh[0][1]), np.sin(dh[3][0])*np.sin(dh[3][1]), dh[3][2]*np.cos(dh[3][0])],
        [np.sin(dh[3][0]), np.cos(dh[3][0])*np.cos(dh[0][1]),-np.cos(dh[3][0])*np.sin(dh[3][1]), dh[3][2]*np.sin(dh[3][0])],
        [               0,                  np.sin(dh[0][1]),                  np.cos(dh[3][1]),                  dh[3][3]],
        [               0,                                 0,                                  0,                         1]
       ]
H4_5 = [
        [np.cos(dh[4][0]),-np.sin(dh[4][0])*np.cos(dh[4][1]), np.sin(dh[4][0])*np.sin(dh[4][1]), dh[4][2]*np.cos(dh[4][0])],
        [np.sin(dh[4][0]), np.cos(dh[4][0])*np.cos(dh[4][1]),-np.cos(dh[4][0])*np.sin(dh[4][1]), dh[4][2]*np.sin(dh[4][0])],
        [               0,                  np.sin(dh[4][1]),                  np.cos(dh[4][1]),                  dh[4][3]],
        [               0,                                 0,                                  0,                         1]
       ]
H5_6 = [
        [np.cos(dh[5][0]),-np.sin(dh[5][0])*np.cos(dh[5][1]), np.sin(dh[5][0])*np.sin(dh[5][1]), dh[5][2]*np.cos(dh[5][0])],
        [np.sin(dh[5][0]), np.cos(dh[5][0])*np.cos(dh[5][1]),-np.cos(dh[5][0])*np.sin(dh[5][1]), dh[5][2]*np.sin(dh[5][0])],
        [               0,                  np.sin(dh[5][1]),                  np.cos(dh[5][1]),                  dh[5][3]],
        [               0,                                 0,                                  0,                         1]
       ]
H0_2 = np.dot(H0_1, H1_2)
H0_3 = np.dot(H0_2, H2_3)
R0_3 = H0_3[:3,:3]
H0_4 = np.dot(H0_3, H3_4)
H0_5 = np.dot(H0_4, H4_5)
H0_6 = np.dot(H0_5, H5_6)
R0_6 = H0_6[:3,:3]
H3_5 = np.dot(H3_4, H4_5)
H3_6 = np.dot(H3_5, H5_6)
#H0_6 = np.dot(H0_5, H5_6)
"""R0_6 = [
        [-1.0, 0.0, 0.0],
        [ 0.0,-1.0, 0.0],
        [ 0.0, 0.0,-1.0]
       ]
"""
"""R0_3 = [
        [-np.sin(T2), 0.0  , np.sin(T2)],
        [ np.cos(T2), 0.0  , np.sin(T2)],
        [0.0        , 1.0  ,        0.0]
       ]
"""
#dwclaring the new value of T2 as found in the inverse kinematics 
#of the first three joint and T1 and T2 still equal to 0
T2 = np.arctan2(Y,X)
#computing the inverse of R0_3 matrix
invR0_3 = np.linalg.inv(R0_3)
#solving for the R3_6 matrix
R3_6 = np.dot(invR0_3, R0_6)
#calculating the angle T5
T5 = np.arccos(R3_6[2][2])
#calculation the angle T6
T6 = np.arccos(-R3_6[2][0]/np.sin(T5))
#calculating the angle T4
T4 = np.arccos(R3_6[1][2]/np.sin(T5))
print(np.matrix(R3_6))
print('theta4=',T4)
print('thata5 =',T5)
print('theta6=',T6)
print(np.matrix(R0_6))
