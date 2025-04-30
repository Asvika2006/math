from pulp import LpProblem, LpVariable, LpMinimize, LpMaximize, lpSum, LpInteger, LpStatus

def solve_operations_research(problem_type, objective_str, constraints_str):
    try:
        # Define the problem
        if problem_type == 'lp':
            prob = LpProblem("LP_Problem", LpMinimize)
        elif problem_type == 'ip':
            prob = LpProblem("IP_Problem", LpMinimize)
        else:
            return "Invalid problem type selected."

        # Define variables (example with x and y)
        if problem_type == 'lp':
            x = LpVariable('x', lowBound=0)
            y = LpVariable('y', lowBound=0)
        else:
            x = LpVariable('x', lowBound=0, cat=LpInteger)
            y = LpVariable('y', lowBound=0, cat=LpInteger)

        # Parse objective function
        objective = eval(objective_str, {"x": x, "y": y, "lpSum": lpSum})
        prob += objective

        # Parse constraints
        constraints = constraints_str.strip().split('\n')
        for constraint in constraints:
            prob += eval(constraint, {"x": x, "y": y})

        # Solve the problem
        prob.solve()

        # Prepare the result
        result = f"Status: {LpStatus[prob.status]}\n"
        result += f"x = {x.varValue}\n"
        result += f"y = {y.varValue}\n"
        result += f"Objective = {prob.objective.value()}"
        return result
    except Exception as e:
        return f"Error: {str(e)}"
