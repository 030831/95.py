a=int(input())
for b in range(1,a+1):
    if b%10==3 or b%10==6 or b%10==9:
        print('X')
    else:
        print(b)


