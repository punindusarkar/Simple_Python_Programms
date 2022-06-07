
# Python function to calculate the factarial of a number (a non-negative integer).

""" def fect0(num):
    fect=1
    if num<0:
        print("Sorry Your Number is nagative")
    elif num==0:
        print("The factorial of 0 is ")
    else:
        for i in range(1,num+1):
            fect=fect*1
            i=i+1
        print("The Factorial of", num,"is", fect)
    return fect

n1=int(input("Enter a number"))

r=fa

fect(n1) """


def fact(n):
    return 1 if (n==1 or n==0) else n* fact(n-1)

num=int(input("Enter Number:"))

print("Factorial:",num,"is",fact(num))


# OutPut

""" Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> python -u "c:\Users\Punindu Sarkar\Desktop\PWP\Programs\24_Factorial_Number.py"
Enter Number:8
Factorial: 8 is 40320
PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs>  """