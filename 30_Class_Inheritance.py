
# Python Program to class Inheritance:

from msilib.schema import Class

class Degree:
    def get(self):
        print("I got a diploma degree")
class Undrgd(Degree):
    def get(self):
        print("I Got a undergraduate degree")
class postgd(Degree):
    def get(self):
        print("I Got a postgradyate degree")

d=Degree()
u=Undrgd()
p=postgd()
d.get()
u.get()
p.get()

# Out Put

""" Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> python -u "c:\Users\Punindu Sarkar\Desktop\PWP\Programs\30_Class_Inheritance.py"
I got a diploma degree
I Got a undergraduate degree
I Got a postgradyate degree 
PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> """
