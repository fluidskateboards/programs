from typing import Optional
class ListNode(object):
    def __init__(self, x=0):
        self.val = x
        self.next = None
def build_linked_list(values):

    dummy = ListNode()
    current = dummy

    for v in values:
        current.next = ListNode(v)
        current = current.next

    return dummy.next
def linked_list_to_list(node):

    result = []

    while node:
        result.append(node.val)
        node = node.next

    return result
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
    l1=build_linked_list([2,4,3])
    l2=build_linked_list([5,6,4])
    res=obj.addTwoNumbers(l1,l2)
    assert linked_list_to_list(res) == [7,0,8]
def test_addtwonums1():
    l1=build_linked_list([0])
    l2=build_linked_list([0])
    res=obj.addTwoNumbers(l1,l2)
    assert linked_list_to_list(res) == [0]
def test_addtwonums2():
    l1=build_linked_list([9,9,9,9,9,9,9])
    l2=build_linked_list([9,9,9,9])
    res=obj.addTwoNumbers(l1,l2)
    assert linked_list_to_list(res) == [8,9,9,9,0,0,0,1]
