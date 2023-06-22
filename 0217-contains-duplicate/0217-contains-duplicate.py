class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if len(nums) == 1:
        #     return False
        # nums.sort()
        # for index in range(len(nums)-1):
        #     if nums[index] == nums[index + 1]:
        #         return True 
        # return False
        hashmap = {}
        for index in range(len(nums)):
            if nums[index] in hashmap:
                return True
            hashmap[nums[index]] = index
        return False