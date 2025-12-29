import random
def logic(nameslist):
    names = nameslist.split()
    y_end = len(names)
    y_turn = 0
    while (len(names) > 1):
        y = y_turn
        bullet = random.randint(1,6) - 1
        # bullet = 0
        revolver = [0,0,0,0,0,0]
        revolver[bullet] = 1
        print("Revolver barrel loaded and spun...")
        print()
        for x in range(0,len(revolver)):
            nameslen = len(names)
            x0 = "-"
            x1 = "-"
            x2 = "-"
            x3 = "-"
            x4 = "-"
            x5 = "-"
            ind = ""
            match x:
                case 0:
                    x0 = "o"
                case 1:
                    x1 = "o"
                case 2:
                    x2 = "o"
                case 3:
                    x3 = "o"
                case 4:
                    x4 = "o"
                case 5:
                    x5 = "o"
            ind = f""" {x0}  {x5}
{x1}    {x4}
 {x2}  {x3}"""
            if y > nameslen - 1:
                y = 0
            print(names[y])
            print(ind)
            input("")
            if revolver[x] == 1:
                print(f"Bang! Thoughts and prayers {names[y]}")
                print()
                names.remove(names[y])
                y_turn = y
                break
            print("Click")
            print()
            y += 1


print("Enter a list of names - Joe Marty Sandy Brenda | one 2 thre{")
script = logic(input())
