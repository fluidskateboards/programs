a=[10,20,30,40,50,60,70,80,90,100]
print(a[3])
print(a[3:5])
print(a[:8])
print(a[2:])
print(a[1:7:3])
print(98 in a)
print(98 not in a)
b = [16,32,64]
print(a + b)
print(a < b)
a += b 
print(a)
c = [16,32,64]
print(b == c)
n = -37
print(bin(n))
print(n.bit_length())
point = (0,3)
print(point[0])
# Type Error
# point[1] = 4
fib = [3,5,8]
print([1,2,*fib, 13,21])
fruits = {'orange':'naranja','pear':'pera','apple':'manzana'}
berries = {'strawberry':'fresa','blueberry':'arandano','blackberry':'mora'}
print({'lemon':'limón',**fruits,**berries,'raspberry':'frambuesa'})
# Syntax Error
# x,y,z = *fib
capitals = {'Chihuahua':'Chihuahua', 'Baja California':'Mexicali','Jalisco':'Guadalajara'}
for state, capital in capitals.items():
    print(f'The capital of {state} is {capital}')
