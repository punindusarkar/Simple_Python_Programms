

# Python script to concatenate following dictionaries to create a new one:

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

dic4={}
for d in (dic1, dic2, dic3,):
    dic4.update(d)
print(dic4)

# OutPut


""" Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> python -u "c:\Users\Punindu Sarkar\Desktop\PWP\Programs\18_Concatenate_dictionaries.py"
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> 
 """
