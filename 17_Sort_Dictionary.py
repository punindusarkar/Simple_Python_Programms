

# Python script to sort (ascending and descending) a dictionary by value:

import operator
d={1:'one',2:'two',3:'three',4:'four',0:'zero'}
print('Original dictionary:',d)

sorted_d=sorted(d.items(),key=operator.itemgetter(0))
print('Dictionary in Asending order by value:',sorted_d)
sorted_d= sorted(d.items(),key=operator.itemgetter(0),reverse=True)
print('Dictionary in descending order by value:',sorted_d)

# Output

""" Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> python -u "c:\Users\Punindu Sarkar\Desktop\PWP\Programs\17_Sort_Dictionary.py"
Original dictionary: {1: 'one', 2: 'two', 3: 'three', 4: 'four', 0: 'zero'}
Dictionary in Asending order by value: [(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]  
Dictionary in descending order by value: [(4, 'four'), (3, 'three'), (2, 'two'), (1, 'one'), (0, 'zero')]
PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs>  """