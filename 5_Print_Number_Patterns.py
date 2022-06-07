
# Print the following patterns using loop:

""" 
        1010101
         10101
          101
           1
           

"""

from ast import Break


i=3
j=0
k=0
while(i>=0):
    a=' '*k+"10"*i+"1"+" "*j
    print(a)
    i=i-1
    j=j+2
    k=k+1
if(i<0 and j>=4):
    Break

# OutPut

""" Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> python -u "c:\Users\Punindu Sarkar\Desktop\PWP\Programs\5_Print_Number_Patterns.py"
1010101
 10101    
  101     
   1      
PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs>  """