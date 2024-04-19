class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for idx in range(len(nums)):
            if nums[idx] in hashmap:
                return True
            hashmap[nums[idx]] = 1
        return False
    
    
        # if len(nums) == 1:
        #     return False
        # nums.sort()
        # for index in range(len(nums)-1):
        #     if nums[index] == nums[index + 1]:
        #         return True 
        # return False