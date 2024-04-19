class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for idx in range(len(nums)):
            if nums[idx] in hashmap:
                hashmap[nums[idx]] += 1
            else:
                hashmap[nums[idx]] = 1
                
        for key,val in hashmap.items():
            if val == 1:
                return key
        
        
        
        # res = 0
        # for n in nums:
        #     res = n ^ res
        # return res
    
    
#         hashmap = {}
#         check = set()
#         for value in nums:
#             if value not in hashmap:
#                 hashmap[value] = 1
#             else:
#                 hashmap[value] += 1
                
#         for key, value in hashmap.items():
#             if value == 1:
#                 return key
                
                
        