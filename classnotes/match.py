# e = 10
# e = 7
# e = (1, "hello", 3)
# e = {"id": 42}
e = 8


match e:
    case 2 | 3 | 5 | 7 | 11:
        print("Small prime")
    case int(n) if n % 5 == 0:
        print("Multiple of 5")
    case(_, x, _):
        print(f"A three-tuple with {x} in the middle")
    case {'id': y}:
        print(f"Your identifier is {y}")
    case _:
        print("What?")