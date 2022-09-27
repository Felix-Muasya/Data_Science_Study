import numpy as np
import matplotlib.pyplot as plt
from empiricaldist import Pmf


hypos = np.linspace(0, 1, 101)
uniform = Pmf(1, hypos, name='unifrom')
uniform.normalize()
ramp_up = np.arange(50)
ramp_down = np.arange(50, -1, -1)
a = np.append(ramp_up, ramp_down)
triangle = Pmf(a, hypos, name='Triangle')
triangle.normalize()
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

update_euro(uniform, dataset)
update_euro(triangle, dataset)

plt.plot(triangle)
plt.plot(uniform)

print(triangle)
plt.show()