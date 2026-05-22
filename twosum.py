class Solution:
    def twosum (self, nums, target):
        hashMap = {}
        for i, v in enumerate(nums):
            diff = target - v 
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[v] = i
obj = Solution()
#using pytest
def test_twosum():
    assert obj.twosum([2,7,11,15],9) == [0,1]
    assert obj.twosum([3,2,4],6) == [1,2]
    assert obj.twosum([3,3],6) == [0,1]