from sympy import symbols, Eq, solve, sympify

def solve_algebra(equations_str):
    try:
        x, y = symbols('x y')
        # Split input into individual equations
        equations_list = equations_str.strip().split('\n')
        equations = []
        for eq_str in equations_list:
            if '=' in eq_str:
                left_str, right_str = eq_str.split('=')
                left_expr = sympify(left_str.strip())
                right_expr = sympify(right_str.strip())
                equation = Eq(left_expr, right_expr)
            else:
                expr = sympify(eq_str.strip())
                equation = Eq(expr, 0)
            equations.append(equation)
        # Solve the system of equations
        solutions = solve(equations, (x, y), dict=True)
        if not solutions:
            return "No solution found."
        return solutions
    except Exception as e:
        return f"Error: {str(e)}"
