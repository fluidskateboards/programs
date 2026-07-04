import random
places = ["beach", "mountain", "city", "forest", "desert"]
def good(place):
    return place in ["beach", "mountain", "forest"]
for place in places:
    if good(place):
        print(f"Ah, a good place: {place}")
        break
else:
    print("No good places for you")

answer = random.randint(1, 100)
tries, guess = 0, None
def malformed(g):
    """Return True if the guess is not valid"""
    if g is None:
        return True
    if not g.strip():           # empty input
        return True
    if not g.isdigit():         # not a number
        return True
    return False
while guess != answer:
    guess = input("What is your guess? ")
    if malformed(guess):
        print("Game over")
        break
    if int(guess) < answer:
        print("Too low")
    elif int(guess) > answer:
        print("Too high")
else:
    print(f"You got it, it was: {guess}")