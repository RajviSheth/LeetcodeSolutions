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
