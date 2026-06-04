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
    def mergeTwoLists (self, list1:Optional[ListNode], list2:Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next
obj = Solution()
#using pytest
def test_mergetwolists():
    l1=build_linked_list([1,2,4])
    l2=build_linked_list([1,3,4])
    res=obj.mergeTwoLists(l1,l2)
    assert linked_list_to_list(res) == [1,1,2,3,4,4]
def test_mergetwolists1():
    l1=build_linked_list([])
    l2=build_linked_list([])
    res=obj.mergeTwoLists(l1,l2)
    assert linked_list_to_list(res) == []
def test_mergetwolists2():
    l1=build_linked_list([])
    l2=build_linked_list([0])
    res=obj.mergeTwoLists(l1,l2)
    assert linked_list_to_list(res) == [0]

