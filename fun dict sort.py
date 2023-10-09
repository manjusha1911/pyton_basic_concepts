def myf(l):
    # return(l["car"])  #car values will be sorted
    return(l["year"])  #years values will be sorted
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myf)
print(cars)