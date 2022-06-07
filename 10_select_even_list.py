
# Python program to select the even items of a list:

list1=[12,3,48,10,36]
even=[]
odd=[]
for j in list1:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
    print("The Even List", even)
    print("The Odd list",odd)



# OutPut

""" 
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> python -u "c:\Users\Punindu Sarkar\Desktop\PWP\Programs\10_select_even_list.py"
The Even List [12]    
The Odd list []       
The Even List [12]    
The Odd list [3]      
The Even List [12, 48]
The Odd list [3]
The Even List [12, 48, 10]
The Odd list [3]
The Even List [12, 48, 10, 36]
The Odd list [3]
PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs>  """