# import datetime as dt
# x=dt.datetime(2023,3,10)
# print(x)  #2023-03-10 00:00:00



import datetime as dt
x=dt.datetime(2023,3,10)  
print(x.strftime("%b"))  #half month(mar.jan,feb,....)
print(x.strftime("%B"))  #full month(march,june,july,.....)
