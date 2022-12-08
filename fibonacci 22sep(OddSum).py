n=int(input())
i=0
a=0
b=1
s=1
print(a)
print(b)
c=a+b
while(c<=n):
    if(i%2==1):
        s=s+c
    i+=1
    print(c)
    a=b
    b=c
    c=a+b
print("Sum of Odd Position Numbers :",s)
    
