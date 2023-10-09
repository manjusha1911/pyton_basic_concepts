# definition
'''
The Fibonacci series is a sequence of numbers in which 
each is the sum of the two preceding ones, usually starting
with 0 and 1.
'''
# example
'''
0=0
1=1
0+1=1
1+1=2
1+2=3
2+3=5
3+5=8
5+8=13
8+13=21
'''

number=int(input("Enter the number:"))
number1=0
number2=1
number3=number1+number2
i=0
while i<=number:
    print(number1)
    number1=number2
    number2=number3
    number3=number1+number2
    i+=1