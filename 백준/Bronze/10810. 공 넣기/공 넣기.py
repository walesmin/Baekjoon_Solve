N, M = map(int, input().split())
N = [0]*(N+1)


for i in range (M):
    i, j, k = map(int, input().split())
    
        
    N [i : j+1] = [k]*(j-i+1)
    
print(*N[1:])