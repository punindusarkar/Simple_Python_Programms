
# Python Program to create a class to print an integer and a charecter:

class Display:
    def smg(self,x,y):
        if type(x)==int:
            print('Integer Message=',x)
        else:
            print('Character Message=',x)
a=Display()
a.smg(20,'Meenakshi')
a.smg('Meenakshi',20)

# Out Put

""" Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> python -u "c:\Users\Punindu Sarkar\Desktop\PWP\Programs\28_Python_class.py"
Integer Message= 20
Character Message= Meenakshi
PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> 
 """