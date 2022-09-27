import pandas as pd
t = pd.DataFrame(index=['Bowl1', 'Bowl2'])
t['prior'] = 0.5, 0.5
t['Likelihood'] = 0.75, 0.5
t['unnorm'] = t['prior']*t['Likelihood']
prop = t['unnorm'].sum()
t['posterior'] = t['unnorm']/prop


print(t)
print(f"the probalility is {prop}")


