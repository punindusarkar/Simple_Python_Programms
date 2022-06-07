
# Print the following patterns using loop:


""" 
            *
        *   *   *
    *   *   *   *   *
        *   *   *
            * 
            
"""

for i in range(3):
    print(' '*(3-i-1)+'*'*(2*i+1))

for j in reversed (range(2)):
    print(' '*(2-j)+'*'*(2*j+1))


#  OutPut

""" 

Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> python -u "c:\Users\Punindu Sarkar\Desktop\PWP\Programs\4_Print_Patterns.py"
  *
 *** 
*****
 *** 
  *  
PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs>  """