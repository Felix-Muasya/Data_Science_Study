import numpy as np
from empiricaldist import Pmf
import matplotlib.pyplot as plt

alpha = 1.0
hypos = np.arange(1, 1001)
prior = Pmf(1, hypos)
ps = hypos**(-alpha)
power = Pmf(ps, hypos, name='power_law')
power.normalize()

hypos = np.arange(1, 1001)
uniform = Pmf(1, hypos, name="unifrom")
uniform.normalize()

def update_train(pmf, data):
    """ updatepmf based on new data"""
    hypos = pmf.qs
    likelihood = 1/hypos
    impossible = (data > hypos)
    likelihood[impossible] = 0
    pmf *= likelihood
    pmf.normalize()


def quantile(pmf, prob):
    """Compute a quantile with the given prob."""
    total = 0
    for q, p in pmf.items():
        total += p
        if total >= prob:
            return q
    return np.nan


dataset = 60
update_train(uniform, dataset)
update_train(power, dataset)
plt.plot(power)
plt.plot(uniform)
#plt.show()

#print(quantile(power, 0.5))
#print(power.quantile([0.05, 0.95]))
print(power.credible_interval(0.9))