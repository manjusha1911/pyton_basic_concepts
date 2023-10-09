n=int(input("enter the number:"))
num=n
sum=0
while num>0:
    rem=num%10
    sum+=rem
    num//=10
if n%sum==0:
    print(n,"is a harshad number")
else:
    print(n,"not a harshad number")
