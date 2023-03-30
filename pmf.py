import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

n = 100
probs = [10**(-3), 0.1, 0.5, 0.7, 0.9]

x = np.arange(0, n+1)
for p in probs:
    pmf_binom = binom.pmf(x, n, p)
    plt.plot(x, pmf_binom)
    plt.title(f"pmf of binomial distribution (p = {p})")
    plt.show()
