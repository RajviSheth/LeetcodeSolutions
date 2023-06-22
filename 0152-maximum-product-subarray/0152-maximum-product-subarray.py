class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = min_so_far = result = nums[0]
        for num in nums[1:]:
            temp = max(num, max_so_far * num, min_so_far * num)
            min_so_far = min(num, max_so_far * num, min_so_far * num)

            max_so_far = temp

            result = max(result, max_so_far)
        return result