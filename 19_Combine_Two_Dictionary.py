

# Python program to combine two dictionary adding values for common keys.

from typing import Container, Counter


d1={ 'a':100, 'b':200, 'c':300}
d2={'a':300, 'b':200, 'd':400}

d1={ 'a':100, 'b':200, 'c':300}
d2={'a':300, 'b':200, 'd':400}

d=Counter(d1) + Counter(d2)
print(d)


# OutPut

""" Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> python -u "c:\Users\Punindu Sarkar\Desktop\PWP\Programs\19_Combine_Two_Dictionary.py"
Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs>  """