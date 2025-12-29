import re
# capricorn = jan 0 - jan 19
# aquarius = jan 20 - feb 18
# pisces = feb 19 - march 20
# aries = march 21 - april 19
# taurus = april 20 - may 20
# gemini = may 21 - june 20
# cancer = june 21 - july 22
# leo = july 23 - august 22
# virgo = august 23 - september 22
# libra = september 23 - oct 22
# scorpio = oct 23 - nov 21
# sagittarius = nov 22 - dec 21
# capricorn = dec 22 - dec 31


class horoscope:
    def sign(date):
        if date <= 19 or date >= 356:
            return "Capricorn"
        if date >= 20 and date <= 49:
            return "Aquarius"
        if date >= 50 and date <= 79:
            return "Pisces"
        if date >= 80 and date <= 109:
            return "Aries"
        if date >= 110 and date <= 140:
            return "Taurus"
        if date >= 141 and date <= 171:
            return "Gemini"
        if date >= 172 and date <= 203:
            return "Cancer"
        if date >= 204 and date <= 234:
            return "Leo"
        if date >= 235 and date <= 265:
            return "Virgo"
        if date >= 266 and date <= 295:
            return "Libra"
        if date >= 296 and date <= 325:
            return "Scorpio"
        if date >= 326 and date <= 355:
            return "Sagittarius"

    def dateToNum(date):
        parsedDate = date.split()
        numDate = re.findall(r'\d+', parsedDate[1])
        if int(numDate[0]) == 0:
            return 0
        if parsedDate[0].lower() == "january":
            return int(numDate[0])
        if parsedDate[0].lower() == "february":
            return 31 + int(numDate[0])
        if parsedDate[0].lower() == "march":
            return 59 + int(numDate[0])
        if parsedDate[0].lower() == "april":
            return 90 + int(numDate[0])
        if parsedDate[0].lower() == "may":
            return 120 + int(numDate[0])
        if parsedDate[0].lower() == "june":
            return 151 + int(numDate[0])
        if parsedDate[0].lower() == "july":
            return 181 + int(numDate[0])
        if parsedDate[0].lower() == "august":
            return 212 + int(numDate[0])
        if parsedDate[0].lower() == "september":
            return 243 + int(numDate[0])
        if parsedDate[0].lower() == "october":
            return 273 + int(numDate[0])
        if parsedDate[0].lower() == "november":
            return 304 + int(numDate[0])
        if parsedDate[0].lower() == "december":
            return 334 + int(numDate[0])
        else:
            return 0

    print("Enter your birthdate: ")
    x = dateToNum(input())
    # print(x)
    if x >= 1 and x <= 365:
        print("Your sign is: " + sign(x))
    else:
        print("Please enter a valid date.")
