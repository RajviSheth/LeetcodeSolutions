class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap = {}
        reverse = {}
        arr = s.split()
        if len(pattern) != len(arr):
            return False
        # print(arr)
        for i in range(len(pattern)):
            if pattern[i] in hashmap:
                if hashmap[pattern[i]] != arr[i]:
                    return False
                
            else:
                if arr[i] in reverse and reverse[arr[i]] != pattern[i]:
                    return False
                hashmap[pattern[i]] = arr[i]
                reverse[arr[i]] = pattern[i]
        return True