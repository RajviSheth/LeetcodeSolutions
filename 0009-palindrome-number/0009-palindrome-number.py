class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        curr = x
        while x:
            digit = x % 10
            x = int(x/10)
            
            res = (res * 10) + digit
            
        print(res)
        print(curr)
            
        if curr == res:
            return True
        
        return False
#         start = 0
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
            
        