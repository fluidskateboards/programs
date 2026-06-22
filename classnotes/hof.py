
def is_odd(x): return x % 2 == 1
def two_x_plus_y(x,y): return x*2 + y
def square(x): return x * x
print(is_odd(7))
print(is_odd(8))
print(two_x_plus_y(3,1))
print(two_x_plus_y(4,0))
print(square(64))
print(square(8))
addSix = lambda x: x + 6
print(addSix(6))
def compose (f, g):
    return lambda x: f(g(x))
def twice(f):
    return compose(f, f)
add_six_then_square = compose(square, addSix)
add_twelve = twice(addSix)
assert add_six_then_square(9) == 225
assert twice(square)(3) == 81
assert add_twelve(100) == 112