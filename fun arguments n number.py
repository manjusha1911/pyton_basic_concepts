def manjusha(*names):
    print(names)
manjusha("sai","ram","baba","krishna","mahadev")


# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def manju(**kids):
    print(kids["mom"],kids["son"])
manju(mom="manjusha",son="nany",daughter="honey")