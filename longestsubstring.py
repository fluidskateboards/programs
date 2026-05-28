class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        letters = set()
        l = 0
        for x in range(len(s)):
            while s[x] in letters:
                letters.remove(s[l])
                l += 1
            letters.add(s[x])
            res = max(res, x - l + 1)
        return res

obj = Solution()
#using pytest
def test_longestsubstring():
    assert obj.lengthOfLongestSubstring("abcabcbb") == 3
    assert obj.lengthOfLongestSubstring("bbbbb") == 1
    assert obj.lengthOfLongestSubstring("pwwkew") == 3
