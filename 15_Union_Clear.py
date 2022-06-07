
# Python program to perform following operations on set: intersection, union, clear.

A={0,2,4,6,8}
B={1,2,3,4,5}

print("Union:", A|B)
print("Intersection:",A&B)
print("Difference:",A-B)
print("Symmetric difference:",A^B)


# OutPut


""" Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> python -u "c:\Users\Punindu Sarkar\Desktop\PWP\Programs\15_Union_Clear.py"
Union: {0, 1, 2, 3, 4, 5, 6, 8}
Intersection: {2, 4}
Difference: {0, 8, 6}
Symmetric difference: {0, 1, 3, 5, 6, 8}
PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs>  """