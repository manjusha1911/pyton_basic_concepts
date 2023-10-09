car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# print(car.get("year"))
p=car.get("year",2023) #we can't update we'll the get old value  
print(p)

p=car.get("thisyear",2023)
print(p)