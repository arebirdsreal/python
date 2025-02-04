#program to find largest of 3 numbers
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a > b and a > c:
    print(f"{a} is largest")
elif b > a and b > c:
    print(f"{b} is largest")
else:
    print(f"{c} is largest")