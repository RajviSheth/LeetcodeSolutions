class Solution:
    def findMin(self, nums: List[int]) -> int:
        # start = 0
        # end = len(nums) - 1
        # while start < end:
        #     if nums[start] > nums[start + 1]:
        #         return nums[start + 1]
        #     elif nums[end] < nums[end - 1]:
        #         return nums[end]
        #     else:
        #         start += 1
        #         end -= 1
        # return nums[0]
        left = 0 
        right = len(nums) - 1
        
        if len(nums) == 1:
            return nums[0]

        if nums[left] < nums[right]:
            return nums[left]
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid -1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
            
            
                 