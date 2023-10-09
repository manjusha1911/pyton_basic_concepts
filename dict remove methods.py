d= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# d.pop("year")
# print(d)

d.popitem()
print(d)

d= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del d["year"]   # sepcified key value will be deleted
# del d  #dict will be deleted
print(d)

d= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
d.clear()
print(d)