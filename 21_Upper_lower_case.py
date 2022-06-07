
# Python function that accepts a string and calculate the number of upper case letter and lower case letters:

def st(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
    else:
        pass
    print("Origianal Stirng:", s)
    print("No. of upper case characters:", d['UPPER_CASE'])
    print("No. of lower case characters:", d['LOWER_CASE'])


    st("Hello Punindu Sarakra")