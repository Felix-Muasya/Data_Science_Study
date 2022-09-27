import numpy as np
from empiricaldist import Pmf

hypos = [6, 8, 12]
prior = Pmf(1/3, hypos)
likelihood = 1/6, 1/8, 1/12
likelihood1 = 0, 1/8, 1/12
posterior = prior*likelihood
posterior *= likelihood1
posterior.normalize()

def update_dice(pmf, data):
    """update pmf based on new data"""
    hypos = pmf.qs
    likelihood = 1/hypos
    impossible = (data > hypos)
    likelihood[impossible] = 0
    pmf *= likelihood
    pmf.normalize()

pmf = prior.copy()
update_dice(pmf, 1)
update_dice(pmf, 3)
update_dice(pmf, 5)
update_dice(pmf, 7)

print(pmf)