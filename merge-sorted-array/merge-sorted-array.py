class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r1 = m -1
        r2 = n-1
        writer = m+n-1
        
        for writer in range(m+n-1, -1, -1):
            if r2 < 0:
                break
            if nums1[r1] > nums2[r2] and r1 >= 0:
                nums1[writer] = nums1[r1]
                r1 -= 1
            else:
                nums1[writer] = nums2[r2]
                r2 -= 1
            
        