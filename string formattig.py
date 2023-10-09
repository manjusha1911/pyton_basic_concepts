'''
The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:
'''


p=49
t="the price is {} dollars"
print(t.format(p))  #the price is 49 dollars


t="the price is {:.2f} dollars"
print(t.format(p))  #the price is 49.00 dollars

name="manjusha"
age=22
place="nellore"
p="my name is {} I'm {} years old and I'm from {}"
print(p.format(name,age,place))

# my name is manjusha I'm 22 years old and I'm from nellore