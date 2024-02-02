class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        while start < end:
            # print(s[start], s[end])
            s[start], s[end] = s[end], s[start]
            # print(s)
            start += 1
            end -= 1
                
                
            
            
            
        