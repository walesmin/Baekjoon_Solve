c = []
while True:
    a,b = map(int, input().split())
    c += [a+b]
    
    if a == 0 and b == 0:
        break


for i in c:
    if i == 0:
        break

    print(i)