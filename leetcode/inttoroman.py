class Solution:
    def intToRoman(self, num):
        roman = [["I", 1],["IV", 4],["V", 5],["IX", 9],["X", 10],["XL", 40],["L", 50],["XC", 90],["C", 100],["CD", 400],["D", 500], ["CM",900],["M", 1000]]
        numerals = ""
        for sym, val in reversed(roman):
            if num // val:
                count = num // val
                numerals = numerals + (sym * count)
                num %= val
        return numerals

obj = Solution()
#using pytest
def test_inttoroman():
    assert obj.intToRoman(3749) == "MMMDCCXLIX"
    assert obj.intToRoman(58) == "LVIII"
    assert obj.intToRoman(1994) == "MCMXCIV"
    assert obj.intToRoman(2001) == "MMI"

