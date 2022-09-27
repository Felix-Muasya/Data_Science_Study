import numpy as np
from empiricaldist import Pmf
import matplotlib.pyplot as plt

hypos = np.linspace(0, 1, 101)
prior = Pmf(1, hypos)

likelihood_heads = hypos
likelihood_tails = 1-hypos

likelihood = {
    'H': likelihood_heads,
    'T': likelihood_tails
}
dataset = 'H' * 140 + 'T' * 110


def update_euro(pmf, dataset):
    """Updatee pmf with a given sequence of H and T"""
    for data in dataset:
        pmf *= likelihood[data]

    pmf.normalize()

posterior = prior.copy()
update_euro(posterior, dataset)

plt.plot(posterior)
plt.show()

