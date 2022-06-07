
# Python program to sum and multiplication of all the items in a list.

sum=0
mul=1
list1=[2,3,4,5,6,7]

for ele in range(0, len(list1)):
    sum=sum + list1[ele]
    mul=mul*list1[ele]
print("Sum Of all elements in given list:",sum)
print("Multiplication of all elements in given list:", mul)


# OutPut


""" Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> python -u "c:\Users\Punindu Sarkar\Desktop\PWP\Programs\7_Sum_&_Multipli_list.py"
Sum Of all elements in given list: 27
Multiplication of all elements in given list: 5040
PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs>  """