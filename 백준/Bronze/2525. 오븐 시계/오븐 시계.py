a,b = map(int, input().split())
c = int(input())

d = (b+ c)/60
e = (b+ c)%60

if b + c < 60 :
    print(a, b+c)

elif b + c >=60 and a+d>=24 :
    print(abs(24-int(a+d)), e)
    
elif b + c >=60 :
    print(int(a+d), e)