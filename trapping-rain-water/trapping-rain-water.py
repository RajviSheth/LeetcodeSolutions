class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxL = height[left]
        maxR = height[right]
        count = 0
        
        while left < right:
            if maxL < maxR:
                left += 1
                maxL = max(maxL, height[left])
                count += maxL - height[left]
            else:
                right -= 1
                maxR = max(maxR, height[right])
                count += maxR - height[right]
                

        return count
            
            
            
        