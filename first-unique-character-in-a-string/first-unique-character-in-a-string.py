class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for value in s:
            if value in hashmap:
                hashmap[value] += 1
            else:
                hashmap[value] = 1
        
        for key, value in enumerate(s):
            if hashmap[value] == 1:
                return key
        return -1
            
        