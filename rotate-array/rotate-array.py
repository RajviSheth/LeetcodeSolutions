class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = [0] * n
        for idx in range(n):
            arr[(idx+k)%n] = nums[idx]
        
        nums[:] = arr
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n = len(nums)
#         a = [0] * n
#         for i in range(n):
#             a[(i + k) % n] = nums[i]
        
#         nums[:] = a
            
# #         for i in range(k):
# #             previous = nums[-1]
# #             for j in range(len(nums)):
# #                 nums[j], previous = previous, nums[j]