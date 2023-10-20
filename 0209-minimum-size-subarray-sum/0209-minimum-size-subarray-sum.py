class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        s, e = 0, 0
        sum_ = nums[s]
        flag = 0
        while e < len(nums):
            if sum_ >= target:
                curr_len = (e - s) + 1
                min_len = min(curr_len, min_len)
                flag = 1
                sum_ -= nums[s]
                s += 1
            else:
                e += 1
                if e == len(nums):
                    break
                sum_ += nums[e]
        if flag == 0:
            return 0
        else:
            return min_len