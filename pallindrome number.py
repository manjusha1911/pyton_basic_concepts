# definition
'''
if a word or sequence reads same from backword as well as forword then it is called
as pallindrome number
'''
# example
'''
121
12321
1234321
'''
num=int(input("Enter the number:"))
number=num
sum=0
while number>0:
    sum=(sum*10)+number%10
    number//=10
print(number)
print(sum)
if num==sum:
    print("pallindrome")
else:
    print("not a pallindrome")