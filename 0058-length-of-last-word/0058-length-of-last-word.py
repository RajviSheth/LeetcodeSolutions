class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pointer = len(s) - 1
        counter = 0
        while s[pointer] == " " and pointer >= 0:
            pointer -= 1
        
        while s[pointer] != " " and pointer >= 0:
            counter += 1
            pointer -= 1
        return counter
        # while pointer > 0:
        #     pointer -= 1
        #     if s[pointer] != " ":
        #         counter += 1
        #     elif counter > 0:
        #         return counter
        # return counter
            
        