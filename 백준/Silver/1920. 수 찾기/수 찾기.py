N = int(input())
NS = set(map(int, input().split()))

M = int(input())
MS = list(map(int, input().split()))

for m in MS:
    if m in NS:
        print("1")
    else:
        print("0")
