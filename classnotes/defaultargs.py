def f(x, y=5, z=10):
    return (x, y, z)
print(f(1))
print(f(1,7))
print(f(1,8,20))
#print(f(1,8,20,40)) Typeerror expected 3 arguments but 4 were given
print(f(x=5,y=10))
print(f(2,z=8))
print(f(z=8,x = 14, y=4))
def line(x1, y1, x2, y2, color="black", thickness=1, style="dotted"):
    return (x1, y1, x2, y2, color, thickness, style)
