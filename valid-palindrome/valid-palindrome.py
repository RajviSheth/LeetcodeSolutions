class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            while start< end and s[start].isalnum() and s[end].isalnum():
                if s[start].lower() == s[end].lower():
                    start += 1
                    end -= 1
                else:
                    return False
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
        return True