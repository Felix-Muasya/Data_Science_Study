from fractions import Fraction
import pandas as pd

table2 = pd.DataFrame(index=[6, 8, 12])
table2['prior'] = Fraction(1, 3)
table2['likelihood'] = Fraction(1, 6), Fraction(1, 8), Fraction(1, 12)
print(table2)

def update(table):
    """compute the posterior probs"""
    table['unnorm'] = table['prior'] * table['likelihood']
    prob_data = table['unnorm'].sum()
    table['posterior'] = table['unnorm']/prob_data
    return prob_data

prob_data = update(table2)

print(table2)