import numpy as np
import math
import random

def inv_kinematics(matrix,link_lengths):
    """
    Given a 4x4 transformation matrix, return 7 parameters (example: 6 joint angles + 1 gripper).
    This is a placeholder; actual UR10e inverse kinematics is complex and requires robot-specific libraries.
    """
    if matrix.shape != (4, 4):
        raise ValueError("Input must be a 4x4 matrix.")

    params = np.zeros(7)  # Placeholder for 7 parameters

    # FINDING THETA 1
    # Lx = X +l6Rzx, Ly = Y + l6Rzy 
    X = -link_lengths[5]*matrix[0,2] + matrix[0,3]
    Y= -link_lengths[5]*matrix[1,2] + matrix[1,3]
    # if we assume cos(alpha) = the common term in X and Y (l2s2 + l3s(2+3) + l5s(2+3+4)/sqrt(l2s2 + l3s(2+3) + l5s(2+3+4)^2 + l4^2)) and sin(alpha) = l4//sqrt(l2s2 + l3s(2+3) + l5s(2+3+4)^2 + l4^2))
    #tan (alpha) = l4/(l2s2 + l3s(2+3) + l5s(2+3+4))
    # X/sqrt(l2s2 + l3s(2+3) + l5s(2+3+4)^2 + l4^2) = c(alpha + theta 1) , Y/sqrt(l2s2 + l3s(2+3) + l5s(2+3+4)^2 + l4^2)= s(alpha + theta 1)
    # params[1] = atan2(Y,X) - alpha
    # to find alpha , let X = Bc1 - As1 , Y= Bs1+Ac1 ( B = l4 , A =l2s2 + l3s(2+3) + l5s(2+3+4)
    # squaring and adding X and Y we get X^2 +Y^2 = B^2 + A^2 , B is a known constant , A is the demoniator of tan(alpha) 
    A = math.sqrt(X**2 + Y**2 + link_lengths[3]**2)
    params[1]=math.atan2(Y,X) - math.atan2(link_lengths[3],A)

    # FINDING THETA 5
    # adding c1Rzx and s1Rzy we get P , P= s5c(2+3+4)
    P = -(matrix[0,2]*math.cos(params[1]) + math.sin(params[1])*matrix[1,2])
    # Rzz = s5s(2+3+4)
    #s5=sqrt(P^2 + rzz^2)
    # subtracting s1Rzx and c1Rzy we get c5 
    params[5] = math.atan2(math.sqrt(A**2 + matrix[2,2]**2), (matrix[0,2]*math.sin(params[1]) + math.cos(params[1])*matrix[1,2]))

    # from the same equation of c1Rzx and s1Rzy = -s5c(2+3+4) diving this by Rzz we get
    # tan(t2+t3+t4) =(matrix[2,2]/P)
    gamma = math.atan2(matrix[2,2], P) # this is theta 2 + theta 3 + theta 4

    # FINDING THETA 6
    # Rxz  and Ryz can help with this , you can either use the same method used for theta 1 or substiture c2+3+4 and s2+3+4 , we know s5
    # with either, we get
    params[6] = math.atan2(-matrix[2,0], matrix[2,1]) - math.atan2(math.cos(params[5])*matrix[2,2],P)

    # FINDING THETA 2,3,4
    # we need d1 input to decouple the equations.
    params[0]=random.random()  # Random initial guess for d1

    M = (matrix[0,3] - link_lengths[5]*matrix[0,2]+ link_lengths[3]*math.sin(params[1]) - link_lengths[4]*math.sin(gamma))/ math.cos(params[1])
    N = matrix[2,3] - link_lengths[0] - params[0] -link_lengths[5]*matrix[2,2] -link_lengths[4]*math.cos(gamma)
    A = (M**2 + N**2 + link_lengths[1]**2 - link_lengths[2]**2)/2*link_lengths[2]
    B = math.sqrt(abs(M**2 + N**2 - A**2))
    params[2] = math.atan2(M, N) - math.atan2(B,A)

    params[3] = math.atan2(M-link_lengths[1]*math.sin(params[2]), N-link_lengths[1]*math.cos(params[2])) - params[2]

    params[4] = gamma - params[2] - params[3]

    return params[:7]

if __name__ == "__main__":
    link_lengths = [0.1807, 0.6127, 0.57155, 0.17415, 0.11985, 0.11655]
    mat = np.array([[-0.e-132, 1.00000000000000, -0.e-134, -0.174150000000000], [-0.707106781186548, -0.e-136, 0.707106781186548, 1.17195436790550], [0.707106781186548, 0.e-131, 0.707106781186548, 0.661610872455082], [0, 0, 0, 1.00000000000000]])
    # mat = np.array([[-0.e-136, 0.e-267, -1.00000000000000, -0.290700000000000], [-0.707106781186548, 0.707106781186548, 0.e-133, 1.08954107255821], [0.707106781186548, 0.707106781186548, 0, 0.579197577107790], [0, 0, 0, 1.00000000000000]])  
    params = inv_kinematics(mat,link_lengths)
    print("Output parameters:", params)