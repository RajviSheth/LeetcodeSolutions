class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for value in s:
            if value in hashmap:
                hashmap[value] += 1
            else:
                hashmap[value] = 1
        for value in t:
            if value in hashmap:
                hashmap[value] -= 1
            else:
                return False
        return all(value == 0 for value in hashmap.values())