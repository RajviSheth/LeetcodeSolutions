class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = collections.Counter(s)
        for value in t:
            if value in count:
                count[value] -= 1
            else:
                return False
        return all(value == 0 for value in count.values())