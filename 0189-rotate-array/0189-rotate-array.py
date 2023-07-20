class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         for i in range(k):
#             previous = nums[-1]
#             for j in range(len(nums)):
#                 nums[j], previous = previous, nums[j]
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
            
        nums[:] = a