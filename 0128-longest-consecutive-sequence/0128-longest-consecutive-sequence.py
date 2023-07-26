class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = sorted(nums)
        # count = 1
        # max_count = 0
        # for index in range(1, len(nums)):
        #     if nums[index] - nums[index-1] == 1:
        #         count += 1
        #     else:
        #         max_count = max(max_count, count)
        #         count = 1
        # return max_count
        
        numSet = set(nums)
        max_count = 0
        for num in nums:
            if (num -1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                max_count = max(length, max_count)
        return max_count
            
        