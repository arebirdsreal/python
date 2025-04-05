N = int(input("Enter size of array: "))
a = [input("Enter element: ") for i in range(N)]
a.sort()
b = []
for j in range(N):
    counter = 0
    temp = a[j]
    while temp not in b:    
        for i in range(N):      
            if temp == a[i]:counter += 1
        print(f"{temp} occurs {counter} times")       
        b.append(temp) 





