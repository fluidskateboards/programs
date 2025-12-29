import random
import sys
class shots():
    def simul(loops):
        maxtotal = sys.maxsize
        maxmade = 0
        worstres = ""
        for x in range(loops):
            res = ""
            count = 0
            count1 = 0
            count2 = 0
            while (count1 != 3):
                num = random.randint(1,4)
                if (num == 1):
                    res += "X "
                    count += 1
                    count1 += 1
                else:
                    res += "O "
                    count1 = 0
                count2 += 1
            if maxtotal > count2:
                maxtotal = count2
                maxmade = count
                worstres = res
            print(res + "\n")
        print(worstres)
        print('Made '+  str(maxmade) + ' shots out of ' + str(maxtotal) )

    simul(1)
