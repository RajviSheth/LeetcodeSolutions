class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        writer = 1
        reader = 0
        
        while reader+1 < len(nums):
            if nums[reader] != nums[reader+1]:
                nums[writer] = nums[reader+1]
                writer += 1
                reader += 1
            else:
                reader += 1
        
        return writer
                