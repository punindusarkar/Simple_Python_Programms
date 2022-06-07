
#  Program to convert bits to Megabytes, Gigabytes, and Terabytes.

b=float(input("Enter Number of Bytes: "))
kb=b/1024
mb=b/(1024*1024)
gb=b/(1024*1024*1024)
tb=b/(1024*1024*1024*1024)

print("Bytes=",b,"Kilobyte=",kb)
print("Bytes=",b,"Megabyte=",mb)
print("Bytes=",b,"Giagbyte=",gb)
print("Bytes=",b,"Terabyte=",tb)

#  OutPut

""" Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs> python -u "c:\Users\Punindu Sarkar\Desktop\PWP\Programs\2_Convert _bits_to_MB_GB.py"
Enter Number of Bytes: 1024
Bytes= 1024.0 Kilobyte= 1.0
Bytes= 1024.0 Megabyte= 0.0009765625
Bytes= 1024.0 Giagbyte= 9.5367431640625e-07  
Bytes= 1024.0 Terabyte= 9.313225746154785e-10
PS C:\Users\Punindu Sarkar\Desktop\PWP\Programs>  """