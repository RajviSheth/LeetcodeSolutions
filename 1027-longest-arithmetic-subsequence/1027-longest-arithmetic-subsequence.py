class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        hashmap = {}
        max_length = 2

        for j in range(len(nums)):
            for i in range(j):
                diff = nums[j] - nums[i]
                if (i, diff) in hashmap:
                    hashmap[(j, diff)] = hashmap[(i, diff)] + 1
                else:
                    hashmap[(j, diff)] = 2
                max_length = max(max_length, hashmap[(j, diff)])

        return max_length