n=int(input("enter the number:"))
num=n
l=len(str(num))
sum=0
while num>0:
    rem=num%10
    sum+=(rem**l)
    num//=10
if sum==n:
    print(n,"is an arm strong number")
else:
    print(n,"not an arm strong number")


