a = int(input())

for i in range(a):
    i += 1
    A,B = map(int, input().split()) 
    print("Case #" +str(i)+":", A+B)
