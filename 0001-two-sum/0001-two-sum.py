class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, value in enumerate(nums):
            difference = target-value
            if difference in hashmap:
                return [idx, hashmap[difference]]
            else:
                hashmap[value] = idx
        
        