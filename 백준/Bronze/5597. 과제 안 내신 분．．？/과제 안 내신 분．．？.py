A = list(range(1,31))
B= []

for i in range(28):
    n = int(input())
    B.append(n)    
 
C = sorted(list(set(A)-set(B)))

print(C[0])
print(C[1])