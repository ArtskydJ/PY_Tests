def triangular(num):
    x=0
    for k in range(num,0,-1):
        x+=k
    return x

for i in range(1,20,1):
    print("num:",i,"fact:",myfactorial(i))
