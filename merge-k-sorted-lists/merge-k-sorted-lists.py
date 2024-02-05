# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for idx in range(0, len(lists), 2):
                l1 = lists[idx]
                l2 = lists[idx+1] if idx+1 < len(lists) else None
                mergedLists.append(self.mergelist(l1, l2))
            lists = mergedLists
            
        return lists[0]
                
    def mergelist(self, l1, l2):
            dummy = ListNode()
            l3 = dummy
            
            while l1 and l2:
                if l1.val < l2.val:
                    l3.next = l1
                    l1 = l1.next
                else:
                    l3.next = l2
                    l2 = l2.next
                l3 = l3.next
            
            if l1:
                l3.next = l1
            if l2:
                l3.next = l2
                
            return dummy.next
                
        