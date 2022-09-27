from empiricaldist import Pmf

prior = Pmf.from_seq(['Bowl 1', 'Bowl 2'])
likelihood_vanilla = [0.75, 0.5]
likelihood_chocolate = [0.25, 0.5]
posterior = prior * likelihood_vanilla
posterior.normalize()
posterior *= likelihood_vanilla
posterior.normalize()
post2 = posterior * likelihood_chocolate
post2.normalize()
print(post2)
print(posterior)
