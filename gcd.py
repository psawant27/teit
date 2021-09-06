def hcf(a, b):
    if(b==0):
        return a
    else:
        return hcf(b, a%b)
a = int(input("Enter a 1st Number : "))
b = int(input("Enter a 2nd Number : "))
print(hcf(a, b))