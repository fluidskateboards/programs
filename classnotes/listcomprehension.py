a = [1,2,10,6]
b = [3,0,4,-8]
print([4 * x for x in a])
print([2 / x + 5 for x in a if x < 4])
print([x + y for x in a for y in b])
print([(x,x**3) for x in a])
print([x + y for x in a for y in b if y <= 0])