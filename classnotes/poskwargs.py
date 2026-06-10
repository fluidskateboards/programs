def f(x, y, z):
    return (x, y, z)
print(f(x=1, y=8, z=20))
print(f(z=1, y=5, x=10))
print(f(20, z=9, y=7))
# print(f(x=1, 2, 3)) syntaxerror positional argument follows keyword argument
def line (x1, y1, x2, y2, color, thickness, style):
    pass
print(line(color="red", thickness=1, style="dashed", x2=9, x1=4, y1=10, y2=8))