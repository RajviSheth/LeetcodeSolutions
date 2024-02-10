class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        check = set()
        for value in nums:
            if value not in hashmap:
                hashmap[value] = 1
            else:
                hashmap[value] += 1
                
        for key, value in hashmap.items():
            if value == 1:
                return key
                
                
        