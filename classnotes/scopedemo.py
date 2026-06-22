dog = "Harley"
rat = "Spencer"
def f():
    dog = "Maverick"
    global rat
    rat = "Chocolate"
    print("In function:", (dog, rat))
print("Outside function:", (dog, rat))
f()
print("Outside function:", (dog, rat))