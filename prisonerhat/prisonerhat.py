import random

prisoners = []
incorrect = 0
count = 0
is_even = True
firstguess = ""
firsttime = True
for i in range(10):
    blackhat = random.randint(0,1)
    if blackhat == 1:
        prisoners.append("Black")
    else:
        prisoners.append("White")
for i in range(1,10):
    if prisoners[i] == "Black":
        count += 1
if count % 2 == 0:
    is_even = True
else:
    is_even = False
print("Zero is an even number.")
print("Guess black if you see an odd number of black hats, white otherwise.")
print(prisoners[1:])
while len(prisoners) > 0:
    print("Guess your hat")
    x = input()
    if x.lower() == prisoners[0].lower():
        prisoners.pop(0)
        if x.lower() == "black" and not firsttime:
            is_even = not is_even
    else:
        print("Incorrect")
        prisoners.pop(0)
        incorrect += 1
    if incorrect > 1:
        print(f"Wrong, the color of your hat was {prisoners[0]}")
        break
    if firsttime:
        firstguess = x.lower()
        firsttime = False
    print(prisoners[1:])
    if is_even and firstguess == "black":
        print("Is Odd")
    elif not is_even and firstguess == "black":
        print("Is Even")
    elif is_even and firstguess == "white":
        print("Is Odd")
    else:
        print("Is Even")
print("Results: " + str(10 - incorrect) + "/10")
print("You survived")