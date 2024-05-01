class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        
        for key, value in enumerate(s):
            if count[value] == 1:
                return key
        return -1
            
        