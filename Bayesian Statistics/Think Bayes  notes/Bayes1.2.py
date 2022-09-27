import pandas as pd
from fractions import Fraction

table_probs = pd.DataFrame(index=[6, 8, 12])
table_probs['prior'] = Fraction(1 , 3)
table_probs['likelihood'] = Fraction(1, 6), Fraction(1, 8), Fraction(1, 12)

def update(table):
    """ Compute the posterior"""
    table['unnorm'] = table['prior'] * table['likelihood']
    prob_data = table['unnorm'].sum()
    table['posterior'] = table['unnorm'] / prob_data
    return prob_data

prob_data = update(table_probs)

print(table_probs)