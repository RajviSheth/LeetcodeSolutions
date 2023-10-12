class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:  
        hashmap = {}
        check = set()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i]in hashmap:
                if t[i] != hashmap[s[i]]:
                    return False
            else:
                if t[i] not in check:
                    check.add(t[i])
                    hashmap[s[i]] = t[i]
                else:
                    return False
        return True
                