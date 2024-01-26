class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0
        for i in range(len(s)):
            # for odd length palindromes
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l + 1) > reslen:
                    reslen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
                
            # for even length
            
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > reslen:
                    reslen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res
        
            
        
#         def ispalindrome(s):
#             start = 0
#             end = len(s)
#             while start < end:
#                 c1 = s[start].lower()
#                 c2 = s[end].lower()
#                 if isvalid(c1) and isvalid(c2):
#                     if c1 != c2:
#                         return False
#                 start += 1
#                 end -= 1
#                 if not isvalid(c1):
#                     start += 1
#                 if not isvalid(c2):
#                     end -= 1
#             return True
        
#         def isvalid(c):
#             return c.isalpha()
            