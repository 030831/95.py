n=int(input())
a=input().split()
for i in range(n):
    a[i]=int(a[i])
for i in range(n-1):
    if(a[i]<a[i+1]):
        a[i+1]=a[i]

print(a[n-1])
