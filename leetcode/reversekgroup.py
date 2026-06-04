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
    def reverseKGroup (self, head:Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev,k)
            if not kth:
                break
            groupNext = kth.next

            prev = kth.next
            curr = groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
obj = Solution()
#using pytest
def test_reversekgroup():
    l1=build_linked_list([1,2,3,4,5])
    res=obj.reverseKGroup(l1,2)
    assert linked_list_to_list(res) == [2,1,4,3,5]
def test_mergetwolists1():
    l1=build_linked_list([1,2,3,4,5,6])
    res=obj.reverseKGroup(l1,3)
    assert linked_list_to_list(res) == [3,2,1,6,5,4]
# def test_mergetwolists2():
#     l1=build_linked_list([])
#     l2=build_linked_list([0])
#     res=obj.mergeTwoLists(l1,l2)
#     assert linked_list_to_list(res) == [0]


