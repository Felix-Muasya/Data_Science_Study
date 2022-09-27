from scipy.stats import binom
import numpy as np
from empiricaldist import Pmf
import matplotlib.pyplot as plt


def make_binomial(n, p):
    """ Make a binomial Pmf"""
    ks = np.arange(n+1)
    ps = binom.pmf(ks, n, p)
    return Pmf(ps, ks)

def prob_get(pmf, threshold):
    """Probability of quantities greater than threshold"""
    get = (pmf.qs >= threshold)
    total = pmf[get].sum()
    return total


pmf_k = make_binomial(n=250, p=0.5)
plt.plot(pmf_k)
print(prob_get(pmf_k, 140))
#plt.show()
#print(pmf_k)
#print(pmf_k[140])