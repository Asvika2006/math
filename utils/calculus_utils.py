from sympy import symbols, diff, integrate, sympify

x = symbols('x')

def solve_calculus(expr, operation):
    try:
        parsed_expr = sympify(expr)
        if operation == 'derivative':
            return f"Derivative: {diff(parsed_expr, x)}"
        elif operation == 'integral':
            return f"Integral: {integrate(parsed_expr, x)}"
        else:
            return "Invalid operation"
    except Exception as e:
        return f"Error: {str(e)}"
