class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        first, sec = 0, 0
        while first < len(s) and sec <len(t):
            if s[first] == t[sec]:
                first += 1
                sec += 1
            else:
                sec += 1
        if first == len(s):
            return True
        return False
        
            
                
            
        