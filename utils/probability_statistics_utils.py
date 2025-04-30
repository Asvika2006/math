import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from scipy import stats

def calculate_statistics(data_str, distribution):
    try:
        # Convert input string to a list of floats
        data = list(map(float, data_str.strip().split(',')))

        # Calculate basic statistics
        mean = np.mean(data)
        median = np.median(data)
        mode = stats.mode(data, keepdims=True).mode[0]
        std_dev = np.std(data)

        # Generate distribution plot
        fig, ax = plt.subplots()
        if distribution == 'normal':
            sns.histplot(data, kde=True, stat="density", linewidth=0)
            sns.kdeplot(data, ax=ax, color='red')
            ax.set_title('Normal Distribution')
        elif distribution == 'binomial':
            n = len(data)
            p = mean / max(data)
            x = np.arange(0, max(data)+1)
            binom_pmf = stats.binom.pmf(x, n, p)
            ax.bar(x, binom_pmf)
            ax.set_title('Binomial Distribution')
        elif distribution == 'poisson':
            lambda_ = mean
            x = np.arange(0, max(data)+1)
            poisson_pmf = stats.poisson.pmf(x, lambda_)
            ax.bar(x, poisson_pmf)
            ax.set_title('Poisson Distribution')
        else:
            return "Invalid distribution selected.", None

        # Save plot to a PNG image in memory
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plot_url = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()

        # Prepare the result
        result = f"""
        Mean: {mean}
        Median: {median}
        Mode: {mode}
        Standard Deviation: {std_dev}
        """
        return result, plot_url
    except Exception as e:
        return f"Error: {str(e)}", None
