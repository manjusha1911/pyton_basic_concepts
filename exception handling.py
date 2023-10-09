
try:
    print(y)
except:
    print("An exception occurred")


try :
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("somthing else went wrong")
