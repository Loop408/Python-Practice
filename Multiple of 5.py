#Checking Multiple of 5 if divisible then decrease by 5
n=list(map(int,input("Enter numbers: ").split(',')))
for i in n:
    if i%5==0:
        i -= 5
    print(i,end=' ')
