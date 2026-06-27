import math
a = [1,2,10,6]
b = [3,0,4,-8]
print([4 * x for x in a])
print([2 / x + 5 for x in a if x < 4])
print([x + y for x in a for y in b])
print([(x,x**3) for x in a])
print([x + y for x in a for y in b if y <= 0])
print([a[i] * b[i] for i in range(len(a))])
print([str(round(355/113.0, i)) for i in range(1,6)])
print([(i, 2**i) for i in range(10)])
print([x for x in [y*y for y in range(10)] if x % 2 == 0])
names = ["ALICE", "BOb", "cAROL", "daVE"]
print([(n.lower(), n.upper()) for n in names])
print([i for i in range(10,30) if i not in range(5,40,2)])
print([(a,b,c) for c in range(1,30) for b in range(1,c) \
 for a in range(1,b) if a*a+b*b==c*c])
integral = [(5,'x',2),(10,'y',5),(7,'s',7)]
print([(i[2]*i[0],i[1],i[2] - 1) for i in integral])
triangle = [(10,5),(4,4),(7,8),(324,54)]
print([t[0]*t[1]/2 for t in triangle])
circle = [5,3,6,10,234,59,34,95]
print([math.pi*(c**2) for c in circle])