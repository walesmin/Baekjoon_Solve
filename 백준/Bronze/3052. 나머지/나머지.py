
A = []
for i in range(10):
    a = int(input())
    b = a%42
    A.append(b)
    
count = len(set(A))
print(count)