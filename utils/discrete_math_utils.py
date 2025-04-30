def solve_discrete_math(problem, parameter):
    try:
        n = int(parameter)
        if problem == 'tower_of_hanoi':
            moves = 2 ** n - 1
            return f"Minimum moves required: {moves}"
        elif problem == 'eight_queens':
            if n != 8:
                return "Eight Queens Puzzle is defined for an 8x8 board."
            return "Number of solutions for 8 Queens Puzzle: 92"
        elif problem == 'no_three_in_line':
            max_points = 2 * n
            return f"Maximum number of points with no three in a line on a {n}x{n} grid: {max_points}"
        else:
            return "Invalid problem selected."
    except ValueError:
        return "Please enter a valid integer for the parameter."
