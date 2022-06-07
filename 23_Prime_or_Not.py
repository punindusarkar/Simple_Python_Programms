
# Python function that takes a number as a parameter and check the number is prime or not.

def prime(n):
    for i in range(2,n+1):
        if n%i==0:
            break
        if i==n:
            print(n,"is Prime Number")
        else:
            print(n,"is not a prime Number")
    return prime
n1=int(input("Enter a number:"))
prime(n1)