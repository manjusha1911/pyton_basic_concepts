# definition:
'''
A palindrome is a word, number, phrase, or other sequence 
of symbols that reads the same backwards as forwards
'''
# example
'''
madam
malayalam
'''
a=input("Enter the word:")
b=a[::-1]
print(b)
if a==b:
    print("Pallindrome")
else:
    print("not a pallindrome")