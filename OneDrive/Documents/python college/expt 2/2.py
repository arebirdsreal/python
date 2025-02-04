#to display even numbers from x to y, take x and y from user
x = int(input("Enter x: "))
y = int(input("Enter y: "))

for i in range(x,y+1):
    if i % 2 == 0:
        print(i)
