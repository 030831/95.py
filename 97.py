w,h=map(int,input().split())
n=int(input())

k=[]
for i in range(w):
    k.append([])
    for j in range(h):
        k[i].append(0)

for i in range(n):
    l,d,x,y=map(int,input().split())
    if d==1:
        for j in range(l):
            k[x+j-1][y-1]+=1
    if d==0:
        for j in range(l):
            k[x-1][y+j-1]+=1
for i in range(w):
    for j in range(h):
        print(k[i][j],end=" ")
    print()


