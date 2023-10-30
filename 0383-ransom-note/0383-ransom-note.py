class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for s in magazine:
            hashmap[s] = hashmap.get(s, 0) + 1
        for s in ransomNote:
            if s in hashmap and hashmap[s] > 0:
                hashmap[s] -= 1
            else:
                return False
        return True