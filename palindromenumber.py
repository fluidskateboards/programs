class Solution:
    def isPalindrome(self,x: int) -> bool:
        string = str(x)
        xlength = len(string)
        res = False
        if xlength % 2 == 0:
            if string[0:int(xlength/2)] == string[int(xlength/2):xlength][::-1]:
                res = True
        else:
            if string[0:int(xlength/2)] == string[int(xlength/2) + 1:xlength][::-1]: # 7 / 2 = 3
                res = True
        return res

obj = Solution()
#using pytest
def test_palindrome():
    assert obj.isPalindrome(121) == True
    assert obj.isPalindrome(-121) == False
    assert obj.isPalindrome(10) == False
    assert obj.isPalindrome(100001) == True

