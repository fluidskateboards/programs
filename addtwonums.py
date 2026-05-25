from typing import Optional
# from some_module import ListNode
class ListNode(object):
    def __init__(self, x=0):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers (self, l1:Optional[ListNode], l2:Optional[ListNode]):
        currNode = ListNode()
        dummy = currNode
        answer, carry = 0, 0 
        while l1 and l2:
            if (l1.val + l2.val + carry) >= 10:
                answer = (l1.val + l2.val + carry) % 10
                carry = 1
            else:
                answer = l1.val + l2.val + carry
                carry = 0
            currNode.next = ListNode(answer)
            currNode = currNode.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            if (l1.val + carry) >= 10:
                answer = (l1.val + carry) % 10
                carry = 1
            else:
                answer = l1.val + carry
                carry = 0
            currNode.next = ListNode(answer)
            currNode = currNode.next
            l1 = l1.next
        while l2:
            if (l2.val + carry) >= 10:
                answer = (l2.val + carry) % 10
                carry = 1
            else:
                answer = l2.val + carry
                carry = 0
            currNode.next = ListNode(answer)
            currNode = currNode.next
            l2 = l2.next
        if carry:
            currNode.next = ListNode(carry)
        return dummy.next
obj = Solution()
#using pytest
def test_addtwonums():
    assert obj.addTwoNumbers([2,4,3],[5,6,4]) == [7,0,8]
    # assert obj.addTwoNumbers([3,2,4],6) == [1,2]
    # assert obj.addTwoNumbers([3,3],6) == [0,1]
