i = int(input())

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dic = {}
for j in range(i):
    m = input()
    v = ''
    if m not in dic:
        for a in range(len(m)):
            v += str(10 + alphabet.index(m[a]))
        dic[m] = int(v)

sorted_dic = sorted(dic.items(), key=lambda x: x[1])
for item in sorted_dic:
    print(item[0])
