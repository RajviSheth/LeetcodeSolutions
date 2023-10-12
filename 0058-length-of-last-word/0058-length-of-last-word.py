class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = list(s)
        pointer = len(s) - 1
        counter = 0
        while s[pointer] == " " and pointer >= 0:
            pointer -= 1
        
        while s[pointer] != " " and pointer >= 0:
            counter += 1
            pointer -= 1
        return counter
            
            
        