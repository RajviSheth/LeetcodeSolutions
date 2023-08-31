from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        charSet = set()
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
                
                
        
        
        
        
        #         chars = Counter()
#         left = 0
#         res = 0
#         right = 0
#         while right < len(s):
#             r = s[right]
#             chars[r] += 1

#             while chars[r] > 1:
#                 l = s[left]
#                 chars[l] -= 1
#                 left += 1

#             res = max(res, right - left + 1)

#             right += 1
#         return res


