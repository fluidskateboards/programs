def g(x, *y):
    return f'x is {x} and y is {y}'
print(g(4))
print(g(3,4))
print(g(8,3,4,5,6,2,3))
def g1(x, **y):
    return f'x is {x} and y is {y}'
print(g1(10))
print(g1(1, a=3, b=5))
print(g1(p='hello',x=8))
# print(g(1,x=5)) TypeError g got multiple values for argument 'x'
def f1(x, *y, z): 
    print(x, y, z) # this makes y the tuple
f1(1,2,3,z=4)
def f2(x, *y, **z): 
    print(x, y, z) # this makes y the tuple and z the dictionary
f2(1,2,3,a=4,b=5 )
def f3(x, *, y, z): 
    print(x, y, z) #this makes y and z take keyword args
f3(10, z=5, y=4 )
def f4(*, x, y, z): 
    print(x, y, z) # this makes x, y, and z take keyword args
f4(z=10, x=5, y=4 )  
def f5(*x, **y): 
    print(x, y) # this makes x the tuple and y the dictionary
f5(10,9,8,7,6,a=5,b=4,c=3)
def f6(*x, y, **z): 
    print(x, y, z) # this makes x the tuple and z the dictionary and requires keyword arg for y
f6(10,9,8,7,y=6,a=5,b=4,c=3)