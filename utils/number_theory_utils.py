from sympy import gcd, lcm, isprime, factorint

def solve_number_theory(operation, numbers_str):
    try:
        numbers = list(map(int, numbers_str.strip().split()))
        if operation == 'gcd':
            result = numbers[0]
            for num in numbers[1:]:
                result = gcd(result, num)
            return f"GCD: {result}"
        elif operation == 'lcm':
            result = numbers[0]
            for num in numbers[1:]:
                result = lcm(result, num)
            return f"LCM: {result}"
        elif operation == 'isprime':
            return f"{numbers[0]} is {'a prime' if isprime(numbers[0]) else 'not a prime'} number."
        elif operation == 'factor':
            factors = factorint(numbers[0])
            return f"Prime Factorization: {factors}"
        else:
            return "Invalid operation."
    except Exception as e:
        return f"Error: {str(e)}"
