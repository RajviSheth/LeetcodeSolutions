class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        # Return the only element or if the array is not rotated (minimum is at index 0).
        if len(nums) == 1 or nums[0] < nums[right]:
            return nums[0]
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If mid element is greater than the rightmost element, the minimum is in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            # If mid element is less than the rightmost element, the minimum is in the left half or at mid.
            elif nums[mid] < nums[right]:
                right = mid
            # When nums[mid] equals nums[right], we cannot determine the minimum half, reduce right by one.
            # This operation does not skip the minimum element because nums[mid] equals nums[right].
            else:
                right -= 1
        
        # After the loop, left == right pointing to the minimum element.
        return nums[left]