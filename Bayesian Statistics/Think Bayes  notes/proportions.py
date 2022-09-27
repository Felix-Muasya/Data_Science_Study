from scipy.stats import binom
import numpy as np
from empiricaldist import Pmf

n = 2
p = 0.5
k = 1

ks = np.arange(n+1)
ans = binom.pmf(ks, n, p)
pmf_k = Pmf(ans, ks)
print(pmf_k)
