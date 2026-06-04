class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

obj = Solution()
#using pytest
def test_lcp():
    assert obj.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert obj.longestCommonPrefix(["dog","racecar","car"]) == ""
    assert obj.longestCommonPrefix(["clutch","cluck","click","clock"]) == "cl"
