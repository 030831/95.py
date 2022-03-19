r,g,b=input().split()
r=int(r)
g=int(g)
b=int(b)
for A in range(0,r):
    for B in range(0,g):
        for C in range(0,b):
            print(A,B,C)
print(r*g*b)