
# Python program that will calculate area and circumference of circle using inbuilt Math module:

import math
r= float(input('Enter the radius of the circle:'))
area = math.pi*r*r
circum=2*math.pi*r
print('Area of tha circle is: %.2f'%area)
print('Cirumference of the circle is: %.2f'%circum)

# Out Put

""" Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> python -u "c:\Users\Punindu Sarkar\Desktop\PWP\Programs\25_Math_Module.py"
Enter the radius of the circle:6
Area of tha circle is: 113.10       
Cirumference of the circle is: 37.70
PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> 
 
"""