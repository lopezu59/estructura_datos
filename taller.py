n = int(input("Type a number:"))
for i in range(1,n+1):
    for q in range (1,i+1):
        print(q,end="")
    print("")

def multiply(a,b):
    total = 0
    for _ in range(abs(b)): 
        total += abs(a)  
    
    
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        total = -total

    return total

print(multiply(3, 4))  
print(multiply(2, 10))  
print(multiply(7, -4))  
print(multiply(-8, -4)) 

def divide(splitting, splitter):
    result = 0
    negative = (splitting < 0) != (splitter < 0)  
    
    splitting, splitter = abs(splitting), abs(splitter)  

    while splitting >= splitter:  
        splitting -= splitter  
        result += 1  
    
    return -result if negative else result 


print(divide(10, 4))  
print(divide(10, -7))  
print(divide(-10, 3))  
print(divide(-10, -2)) 
print(divide(7, 3))    

