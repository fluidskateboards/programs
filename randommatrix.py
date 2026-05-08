import random
#using list comprehension
two_d_list = [[0 for _ in range(3)]for _ in range(3)]
for x in range(3):
    for y in range(3):
        two_d_list[x][y] = random.randint(1,10)
for i in range(len(two_d_list)):
    print(two_d_list[i])        
