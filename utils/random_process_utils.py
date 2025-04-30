import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def solve_random_process(process_type, parameter):
    try:
        n = int(parameter)
        if process_type == 'poisson':
            # Simulate a Poisson process
            lam = 5  # rate parameter
            intervals = np.random.exponential(1/lam, n)
            arrival_times = np.cumsum(intervals)
            return f"Simulated Poisson process arrival times: {arrival_times}"
        elif process_type == 'markov':
            # Simple 2-state Markov chain simulation
            states = [0, 1]
            transition_matrix = [[0.9, 0.1], [0.5, 0.5]]
            current_state = 0
            state_sequence = [current_state]
            for _ in range(n - 1):
                current_state = np.random.choice(states, p=transition_matrix[current_state])
                state_sequence.append(current_state)
            return f"Simulated Markov chain states: {state_sequence}"
        elif process_type == 'random_walk':
            # Simulate a simple random walk
            steps = np.random.choice([-1, 1], size=n)
            position = np.cumsum(steps)
            # Plotting the random walk
            plt.figure()
            plt.plot(position)
            plt.title('Random Walk')
            plt.xlabel('Step')
            plt.ylabel('Position')
            # Save plot to a PNG image in memory
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            image_base64 = base64.b64encode(buf.read()).decode('utf-8')
            plt.close()
            return f'<img src="data:image/png;base64,{image_base64}" alt="Random Walk">'
        else:
            return "Invalid process type selected."
    except ValueError:
        return "Please enter a valid integer for the parameter."
