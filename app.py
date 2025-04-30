from flask import Flask, render_template,request
from utils.calculus_utils import solve_calculus
from utils.algebra_utils import solve_algebra
from utils.number_theory_utils import solve_number_theory
from utils.discrete_math_utils import solve_discrete_math
from utils.random_process_utils import solve_random_process
from utils.operations_research_utils import solve_operations_research
from utils.probability_statistics_utils import calculate_statistics

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

if __name__ == '__main__':
    app.run(debug=True)
