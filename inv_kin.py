import numpy as np
import math

def inv_kinematics(matrix,link_lengths):
    """
    Given a 4x4 transformation matrix, return 7 parameters (example: 6 joint angles + 1 gripper).
    This is a placeholder; actual UR10e inverse kinematics is complex and requires robot-specific libraries.
    """
    if matrix.shape != (4, 4):
        raise ValueError("Input must be a 4x4 matrix.")

    params = np.zeros(7)  # Placeholder for 7 parameters
    # substitute for alpha

    alpha = math.atan2(link_lengths[1]*params[2]+link_lengths[2]*math.sin(params[2]+params[3])+link_lengths[4]*matrix[2,2]/maths.sin(params[5]),link_lengths[3])
    beta= math.atan2(matrix[1,2],-matrix[0,2]) - params[1]
    gamma = mat.atan2(math.cos(params[5]*math.tan(params[2]+params[3]+params[4])))

    params[1]=math.atan2((-link_lengths[5]*matrix[0,2] + matrix[0,3]),(-link_lengths[5]*matrix[1,2] + matrix[1,3])) - alpha
    params[6]=math.atan2(matrix[2,1],-matrix[2,0])-gamma


    return params[:7]

if __name__ == "__main__":
    link_lengths = [0.1807, 0.6127, 0.57155, 0.17415, 0.11985, 0.11655]
    mat = np.array([[-0.e-132, 1.00000000000000, -0.e-134, -0.174150000000000], [-0.707106781186548, -0.e-136, 0.707106781186548, 1.17195436790550], [0.707106781186548, 0.e-131, 0.707106781186548, 0.661610872455082], [0, 0, 0, 1.00000000000000]])
    params = inv_kinematics(mat,link_lengths)
    print("Output parameters:", params)