a = int(input())
b = int(input())
sum = 0

for i in range(1, b+1):
    i, n = map(int, input().split())
    sum += i*n
    
if a == sum:
    print("Yes")
else :
    print("No") 