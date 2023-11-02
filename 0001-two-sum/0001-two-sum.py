class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap = {}
        # for index in range(len(nums)):
        #     complement = target - nums[index]
        #     if complement in hashmap:
        #         return index, hashmap[complement]
        #     hashmap[nums[index]] = index

        hashmap = {}
        for idx in range(len(nums)):
            complement = target - nums[idx]
            if complement in hashmap:
                return [idx, hashmap[complement]]
            else:
                hashmap[nums[idx]] = idx
        