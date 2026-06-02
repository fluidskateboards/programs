class Solution:
    def isValid(self, s):
        parenList = []
        parenChars = {'{':'}','[':']','(':')'}
        for i in s:
            if not parenList and i in parenChars:
                parenList.append(i)
            else:
                if (not parenList and i not in parenChars) or len(s) % 2 == 1:
                    return False
                if(parenChars[parenList[-1]] == i):
                    parenList.pop()
                elif i in parenChars:
                    parenList.append(i)
                else:
                    return False
        return not parenList

obj = Solution()
#using pytest
def test_isValid():
    assert obj.isValid("()") == True
    assert obj.isValid("()[]{}") == True
    assert obj.isValid("(]") == False
    assert obj.isValid("([])") == True
    assert obj.isValid("([)]") == False


