# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1
        count -= n
        ptr = dummy
        while count > 0:
            ptr = ptr.next
            count -= 1
        ptr.next = ptr.next.next
        return dummy.next