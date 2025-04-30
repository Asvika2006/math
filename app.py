from flask import Flask, Flask, render_template, request, jsonify, redirect, url_for, flash, session
from utils.calculus_utils import solve_calculus
from utils.algebra_utils import solve_algebra
from utils.number_theory_utils import solve_number_theory
from utils.discrete_math_utils import solve_discrete_math
from utils.random_process_utils import solve_random_process
from utils.operations_research_utils import solve_operations_research
from utils.probability_statistics_utils import calculate_statistics
import math
import re
import json
import numpy as np
from datetime import datetime
from functools import wraps
import logging
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculus', methods=['GET', 'POST'])
def calculus():
    result = None
    if request.method == 'POST':
        expression = request.form['expression']
        operation = request.form['operation']
        result = solve_calculus(expression, operation)
    return render_template('calculus.html', result=result)

@app.route('/algebra', methods=['GET', 'POST'])
def algebra():
    result = None
    if request.method == 'POST':
        equations = request.form['equations']
        result = solve_algebra(equations)
    return render_template('algebra.html', result=result)

@app.route('/number-theory', methods=['GET', 'POST'])
def number_theory():
    result = None
    if request.method == 'POST':
        operation = request.form['operation']
        numbers = request.form['numbers']
        result = solve_number_theory(operation, numbers)
    return render_template('number_theory.html', result=result)

@app.route('/discrete-math', methods=['GET', 'POST'])
def discrete_math():
    result = None
    if request.method == 'POST':
        problem = request.form['problem']
        parameter = request.form['parameter']
        result = solve_discrete_math(problem, parameter)
    return render_template('discrete_math.html', result=result)

@app.route('/random-process', methods=['GET', 'POST'])
def random_process():
    result = None
    if request.method == 'POST':
        process_type = request.form['process_type']
        parameter = request.form['parameter']
        result = solve_random_process(process_type, parameter)
    return render_template('random_process.html', result=result)

@app.route('/operations-research', methods=['GET', 'POST'])
def operations_research():
    result = None
    if request.method == 'POST':
        problem_type = request.form['problem_type']
        objective = request.form['objective']
        constraints = request.form['constraints']
        result = solve_operations_research(problem_type, objective, constraints)
    return render_template('operations_research.html', result=result)

@app.route('/probability-statistics', methods=['GET', 'POST'])
def probability_statistics():
    result = None
    plot_url = None
    if request.method == 'POST':
        data = request.form['data']
        distribution = request.form['distribution']
        result, plot_url = calculate_statistics(data, distribution)
    return render_template('probability_statistics.html', result=result, plot_url=plot_url)

app.secret_key = os.environ.get('SECRET_KEY', 'dev_key_for_mathintel')  # In production, set via environment variable

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
MAX_HISTORY_SIZE = 10

# Custom Math Functions
def factorial(n):
    """Calculate factorial with input validation"""
    if not isinstance(n, (int, float)) or n != int(n) or n < 0:
        raise ValueError("Factorial requires a non-negative integer")
    if n > 170:  # Prevent overflow
        raise ValueError("Value too large for factorial calculation")
    return math.factorial(int(n))

def log2(x):
    """Logarithm base 2"""
    return math.log(x, 2)

def log10(x):
    """Logarithm base 10"""
    return math.log10(x)

def ln(x):
    """Natural logarithm"""
    return math.log(x)

def average(*args):
    """Calculate the average of a list of numbers"""
    if not args:
        raise ValueError("Cannot compute average of empty sequence")
    return sum(args) / len(args)

def std_dev(*args):
    """Calculate the standard deviation"""
    if len(args) < 2:
        raise ValueError("Standard deviation requires at least two values")
    return np.std(args)

def gcd(a, b):
    """Greatest common divisor"""
    a, b = int(a), int(b)
    return math.gcd(a, b)

def lcm(a, b):
    """Least common multiple"""
    a, b = int(a), int(b)
    return abs(a * b) // math.gcd(a, b)

# Define safe math functions dictionary
SAFE_FUNCTIONS = {
    # Constants
    'pi': math.pi,
    'e': math.e,
    'tau': math.tau,
    'inf': math.inf,
    'nan': math.nan,
    
    # Basic math
    'abs': abs,
    'round': round,
    'min': min,
    'max': max,
    'sum': sum,
    
    # Trigonometric functions
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'asin': math.asin,
    'acos': math.acos,
    'atan': math.atan,
    'atan2': math.atan2,
    'sinh': math.sinh,
    'cosh': math.cosh,
    'tanh': math.tanh,
    'asinh': math.asinh,
    'acosh': math.acosh,
    'atanh': math.atanh,
    
    # Logarithmic and exponential functions
    'exp': math.exp,
    'log': math.log,
    'log10': log10,
    'log2': log2,
    'ln': ln,
    
    # Power and roots
    'pow': math.pow,
    'sqrt': math.sqrt,
    'cbrt': lambda x: x ** (1/3),  # Cube root
    
    # Number theory
    'factorial': factorial,
    'gcd': gcd,
    'lcm': lcm,
    'ceil': math.ceil,
    'floor': math.floor,
    'trunc': math.trunc,
    'fmod': math.fmod,
    'degrees': math.degrees,
    'radians': math.radians,
    
    # Statistical functions
    'average': average,
    'std': std_dev,
    
    # Conversion functions
    'int': int,
    'float': float
}

def safe_eval(expr):
    """
    Safely evaluate a mathematical expression using a custom parser
    instead of Python's eval() function
    """
    # Pre-process to handle special cases
    expr = expr.replace('^', '**')  # Replace ^ with ** for exponentiation
    expr = expr.replace('π', 'pi')  # Replace π with pi
    
    # Remove any invalid characters
    clean_expr = re.sub(r'[^0-9+\-*/().,\s\w]', '', expr)
    
    # Validate input before evaluation (only allow alphanumeric, operators, and some special chars)
    if not re.match(r'^[\w\s+\-*/(),.\[\]**]+$', clean_expr):
        raise ValueError("Invalid characters in expression")
    
    # Check for potentially dangerous patterns
    dangerous_patterns = [
        r'__.*__',           # Dunder methods
        r'import',           # Import statements
        r'exec',             # Code execution
        r'eval',             # Nested evaluation
        r'getattr',          # Attribute access
        r'open',             # File operations
        r'globals',          # Global namespace access
        r'locals',           # Local namespace access
    ]
    
    for pattern in dangerous_patterns:
        if re.search(pattern, clean_expr):
            raise ValueError("Potentially unsafe expression")
    
    # Evaluate using our safe functions dictionary
    try:
        # Create a safe globals dict with our allowed functions
        safe_globals = {"__builtins__": {}}
        safe_globals.update(SAFE_FUNCTIONS)
        
        # Use Python's eval with our restricted environment
        result = eval(clean_expr, safe_globals)
        
        # Ensure the result is a reasonable numeric value
        if isinstance(result, (int, float, complex)):
            # Format large integers and floats for better readability
            if isinstance(result, int) and abs(result) > 1000000:
                result = f"{result:,}"
            elif isinstance(result, float):
                # Format floating point for better precision display
                if abs(result) < 0.0001 or abs(result) > 1000000:
                    result = f"{result:.10e}"
                else:
                    result = round(result, 10)
                    # Remove trailing zeros
                    if result == int(result):
                        result = int(result)
            return result
        else:
            return result
    except Exception as e:
        logger.warning(f"Evaluation error: {e} for expression: {expr}")
        raise ValueError(f"Evaluation error: {str(e)}")

def save_calculation_history(expression, result):
    """Save calculation to history in session"""
    if 'calculation_history' not in session:
        session['calculation_history'] = []
    
    # Create a new history entry
    history_entry = {
        'expression': expression,
        'result': str(result),
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Add to the beginning of the list
    history = session['calculation_history']
    history.insert(0, history_entry)
    
    # Keep only the most recent entries
    if len(history) > MAX_HISTORY_SIZE:
        history = history[:MAX_HISTORY_SIZE]
    
    session['calculation_history'] = history
    session.modified = True

def get_calculation_history():
    """Get calculation history from session"""
    return session.get('calculation_history', [])

@app.route('/', methods=['GET'])
def index():
    """Render the home page"""
    return render_template('home.html')

@app.route('/tools', methods=['GET', 'POST'])
def calculator():
    """Handle calculator requests"""
    result = ''
    error = None
    expression = ''
    
    if request.method == 'POST':
        expression = request.form.get('expression', '')
        
        try:
            # Validate input length to prevent abuse
            if len(expression) > 500:
                raise ValueError("Expression too long")
            
            result = safe_eval(expression)
            save_calculation_history(expression, result)
            logger.info(f"Calculation success: {expression} = {result}")
            
        except Exception as e:
            error = str(e)
            logger.warning(f"Calculation error: {error} for expression: {expression}")
            result = f"Error: {error}"
    
    return render_template(
        'calculator.html',
        result=result,
        error=error,
        expression=expression,
        history=get_calculation_history()
    )

@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    """API endpoint for calculations"""
    data = request.get_json()
    
    if not data or 'expression' not in data:
        return jsonify({'error': 'No expression provided'}), 400
    
    expression = data['expression']
    
    try:
        result = safe_eval(expression)
        save_calculation_history(expression, result)
        return jsonify({
            'expression': expression,
            'result': result,
            'success': True
        })
    except Exception as e:
        logger.warning(f"API calculation error: {e} for expression: {expression}")
        return jsonify({
            'expression': expression,
            'error': str(e),
            'success': False
        }), 400

@app.route('/clear-history', methods=['POST'])
def clear_history():
    """Clear calculation history"""
    if 'calculation_history' in session:
        session.pop('calculation_history')
        flash('Calculation history cleared', 'success')
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'success': True})
    
    return redirect(url_for('calculator'))

@app.route('/tools/graphing-calculator')
def graphing_calculator():
    """Render the graphing calculator page"""
    return render_template('graphing_calculator.html')

@app.route('/tools/matrix-calculator')
def matrix_calculator():
    """Render the matrix calculator page"""
    return render_template('matrix_calculator.html')

@app.route('/tools/equation-solver')
def equation_solver():
    """Render the equation solver page"""
    return render_template('equation_solver.html')

@app.route('/tools/unit-converter')
def unit_converter():
    """Render the unit converter page"""
    return render_template('unit_converter.html')
if __name__ == '__main__':
    app.run(debug=True)
