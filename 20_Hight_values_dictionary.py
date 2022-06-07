

# Python Program to find the hight values in a dictionary.

from heapq import nlargest
dic1 = {'a':500, 'b':600, "c":560, 'd':400, 'e':800, 'f':20}
largest3= nlargest(3, dic1, key=dic1.get)
print(largest3)

# Out Put

""" Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> python -u "c:\Users\Punindu Sarkar\Desktop\PWP\Programs\20_Hight_values_dictionary.py"
['e', 'b', 'c']
PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs>  """