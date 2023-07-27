N, M = map(int, input().split())
N = list(range(1,N+1))

for i in range(M):
    i, j = map(int, input().split())
    a= N[i-1]
    b= N[j-1]
    N[j-1]= a
    N[i-1]= b
    
    
print(*N[0:])