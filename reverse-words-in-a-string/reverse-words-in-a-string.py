class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
#         res = ''
#         s1 = len(s) - 1
#         e1 = len(s) - 1
        
#         while e1 and s1:
#             while s[e1] == ' ':
#                 e -= 1
                
        
#         while s1 and e1:
#             while e1 and s[e1] != ' ':
#                 e1 -= 1
#             res += s[e1+1:s1+1]
#             res += ' '
#             print(res)
#             while e1 and s[e1] == ' ':
#                 e1 -= 1
#                 s1 -= 1
            
#             s1 = e1
            
#         return res