#ValueError: invalid literal for int() with base 10: 'coffee'
# Python is trying to turn the string into an int, and is looking for digits in
# base 10 (0-9). It throws a ValueError in frustration.
print(int("coffee"))
#ValueError: invalid literal for int() with base 20: 'coffee'
# Must be between base 2 and base 32. 32 - (A-7). 
# Not sure what base 20 looks like. Maybe (0-J)?
print(int("coffee", 20))
