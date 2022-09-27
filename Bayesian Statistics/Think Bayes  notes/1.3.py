from uno import *

table3 = pd.DataFrame(index=['Door 1', 'Door 2', 'Door 3'])
table3['prior'] = Fraction(1, 3)
table3['likelihood'] = Fraction(1, 2), 1, 0
update(table3)

print(table3)