import numpy as np
from empiricaldist import Pmf
import matplotlib.pyplot as plt
hypos = np.arange(1, 1001)
prior = Pmf(1, hypos)


def update_train(pmf, data):
    """ updatepmf based on new data"""
    hypos = pmf.qs
    likelihood = 1/hypos
    impossible = (data > hypos)
    likelihood[impossible] = 0
    pmf *= likelihood
    pmf.normalize()

data = 60
posterior = prior.copy()
update_train(posterior, data)
print(posterior.max_prob())
plt.plot(posterior)
#plt.show()

mean = np.sum(posterior.ps * posterior.qs)
print(mean)
print(posterior.mean())