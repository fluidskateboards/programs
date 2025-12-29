def longDiv (num, denom):
    currentNum = ""
    res = ""
    iteration = 0
    for i in range(len(str(num))):
        currentNum += str(num)[i]
        if int(currentNum) >= denom:
            print(currentNum)
            iteration = 0
            while True:
                if(int(currentNum) < denom):
                    break
                currentNum = str(int(currentNum) - denom)
                iteration += 1
            res += str(iteration)
        else:
            if(len(currentNum) < 1):
                res += str(0)
        print(iteration)
        iteration = 0
    print(f"{num} / {denom} is: {float(num)/denom}")
    return (f"{res} r{currentNum}")

def interface():
    args = input("format - numerator denominator")
    args = args.split()
    print(longDiv(int(args[0]),int(args[1])))

interface()
