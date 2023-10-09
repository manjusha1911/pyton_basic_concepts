age=22
place="nellore"
name="manjusha"
salary=49
p="my name is {2} i am from {1} my age is {0} my salary is {3:.2f}"
print(p.format(age,place,name,salary))
p="her name is {0} , {0} came from {1}"
print(p.format(name,place))


# named indexing

p="my name is {name} i am from {place}"
print(p.format(name="manjusha",place="nellore"))