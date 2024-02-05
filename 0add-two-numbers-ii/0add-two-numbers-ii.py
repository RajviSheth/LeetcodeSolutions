# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []
        s3 = []
        carry = 0
        
        while l1 or l2:
            if l1:
                s1.append(l1.val)
            if l2:
                s2.append(l2.val)
                
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        while s1 or s2 or carry:
            v1 = s1.pop() if s1 else 0
            v2 = s2.pop() if s2 else 0
            
            val = v1 + v2 + carry
            carry = val//10
            val = val%10
            
            s3.append(val)
        
        dummy = ListNode()
        curr = dummy
        while s3:
            value = s3.pop()
            curr.next = ListNode(value)
            curr = curr.next
            
        return dummy.next
            
        
            
            
            
            
        