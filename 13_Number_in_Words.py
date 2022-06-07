
# Print the number in words for example:1234=> One Two Three Four.

ones=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
num= input("Enter a Number")
print(num)
word=[]
for a in num:
    word.append(ones[int(a)])
print(word)



# OutPut

""" Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> python -u "c:\Users\Punindu Sarkar\Desktop\PWP\Programs\13_Number_in_Words.py"
Enter a Number1234
1234
['One', 'Two', 'Three', 'Four']
PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs>  """