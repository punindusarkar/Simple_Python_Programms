
# Python program to create a class print area of rectangle:

class Area:
    def printArea (self,x,y=None):
        if y is not None:
            print("Area Of  Rectangle=", x*y)
        else:
            print("Area of Square=",x*x)
a=Area()
a.printArea(10)
a.printArea(10,20)


# OutPut

""" Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> python -u "c:\Users\Punindu Sarkar\Desktop\PWP\Programs\29_Rectangle_Class.py"
Area of Square= 100    
Area Of  Rectangle= 200
PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> 
 """
