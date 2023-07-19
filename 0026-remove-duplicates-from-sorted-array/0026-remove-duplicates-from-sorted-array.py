class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
#         check = set()
#         writer = 0
        
#         for reader in range(len(nums)):
#             if nums[reader] not in check:
#                 check.add(nums[reader])
#                 nums[writer] = nums[reader]
#                 writer += 1
            
#         return writer
        insertidx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[insertidx] = nums[i]
                insertidx += 1
        return insertidx