n = int(input("Enter n:")) 
odd = [] 
even = [] 
total = 0 
for i in range(n): 
    if(i%2 == 0): 
        even.append(i) 
        #x= even.count()
    else: 
        odd.append(i) 
    total += i 
print("Even numbers:",*even) 
print("Odd numbers:",*odd) 
