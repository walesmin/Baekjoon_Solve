a,b = map(int, input().split())

if b>= 45:  
    print(a, b-45)

elif b<45 and a>0:
    print(a-1, 60+b-45)

elif b<45 and a==0:
    print("23", 60+b-45)