d =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in d:
    print(x)  #keys
    print(d[x])  #values
print()

for x in d.keys():
    print(x)
print()
for y in d.values():
    print(y)

for x,y in d.items():
    print(x,y)