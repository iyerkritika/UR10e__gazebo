from sympy import symbols, cos, sin, Matrix, simplify
import sympy

def dh_transform(a, alpha, d, t):
    
    T = Matrix([
        [cos(t), -sin(t),  0, a],
        [sin(t)*cos(alpha), cos(t)*cos(alpha), -sin(alpha), -d*sin(alpha)],
        [sin(t)*sin(alpha), cos(t)*sin(alpha), cos(alpha),d*cos(alpha)],
        [0,           0,                      0,                     1]
    ])
    return simplify(T)

if __name__ == "__main__":

    dh_params = Matrix([
    [0,0,symbols('d1'),0],
    [0,0,symbols('l1'),symbols('t1')],
    [0,-sympy.pi/2,0,-sympy.pi/2+symbols('t2')],
    [symbols('l2'),0,0,symbols('t3')],
    [symbols('l3'),0,symbols('l4'),sympy.pi/2+symbols('t4')],
    [0,sympy.pi/2,symbols('l5'),symbols('t5')],
    [0,-sympy.pi/2,symbols('l6'),symbols('t6')]
    ])
    
    # # Substitute example values for all symbols in final_mat
    subs_dict = {
        'l1':0.1807,'l2': 0.6127, 'l3': 0.57155, 'l4': 0.17415, 'l5': 0.11985, 'l6': 0.11655,
        'd1': 0.05,'t1':sympy.pi/2, 't2': sympy.pi/4, 't3': sympy.pi/4, 't4': sympy.pi/4, 't5': sympy.pi/2, 't6': sympy.pi/2
    }

    final_mat = Matrix.eye(4)
    for i in range(dh_params.rows):
        a, alpha, d, t = dh_params.row(i)
        T = dh_transform(a, alpha, d, t)
        final_mat = simplify(final_mat*T)

    #setting up for testing inv kinematics
    # print("Final Transformation Matrix:")
    # print(final_mat.evalf(subs=subs_dict))

    for i in range(final_mat.rows):
        for j in range(final_mat.cols):
            print(f"final_mat[{i}][{j}] = {final_mat[i, j]}")
            input("Press Enter to continue...")  # Pause after each element
