'''
JavaScript Object Notation
'''

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(x)
#O/P
# None, 'cars': [{'model': 'BMW 230', 'mpg': 27.5}, {'model': 'Ford Edge', 'mpg': 24.1}]}
print(json.dumps(x)) 
#{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}

y = json.dumps(x)
print(y)
#{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}



# without JSON
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(x)

#{'name': 'John', 'age': 30, 'married': True, 'divorced': False, 'children': ('Ann', 'Billy'), 'pets': None, 'cars': [{'model': 'BMW 230', 'mpg': 27.5}, {'model': 'Ford Edge', 'mpg': 24.1}]}