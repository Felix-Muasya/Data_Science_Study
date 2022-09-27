import numpy as np
from empiricaldist import Pmf

hypos = np.arange(101)
prior = Pmf(1, hypos)
prior.normalize()
likelihood_vanilla = hypos/100
likelihood_chocolate = 1 - hypos/100
posterior1 = prior * likelihood_vanilla
posterior1.normalize()
posterior2 = posterior1 * likelihood_vanilla
posterior2.normalize()
posterior3 = posterior2 * likelihood_chocolate
posterior3.normalize()

print(prior)
print(likelihood_vanilla[:5])
print(posterior1.head())
print(posterior2)
print(posterior3)