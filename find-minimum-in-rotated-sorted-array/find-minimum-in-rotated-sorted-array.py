class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        
#         if len(nums) == 1 or nums[0] < nums[right]:
#             return nums[0]
        
#         while left < right:
#             mid = left + (right - left) // 2
        
#             if nums[mid] > nums[right]:
#                 left = mid + 1
            
#             elif nums[mid] < nums[right]:
#                 right = mid
            
#             else:
#                 right -= 1
        
#         return nums[left]
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[right]:
            return nums[0]
        
        while left <= right:
            mid = left + (right-left) //2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid -1]> nums[mid]:
                return nums[mid]
            if nums[mid] > nums[left]:
                left = mid+1
            else:
                right = mid-1
                
            
                 