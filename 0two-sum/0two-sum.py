class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, value in enumerate(nums):
            diff = target - value
            if diff in hashmap:
                return [idx, hashmap[diff]]
            else:
                hashmap[value] = idx
        