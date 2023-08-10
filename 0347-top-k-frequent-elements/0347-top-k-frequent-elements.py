class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for value in nums:
            count[value] = 1 + count.get(value, 0)
            
        for n,c in count.items():
            freq[c].append(n)
            
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                
                if len(res) == k:
                    return res
        
#         if k == len(nums):
#             return nums
#         dict_count = Counter(nums)
#         sorted_dict = sorted(dict_count.items(), key=lambda item:item[1], reverse=True)
        
#         top_k_items = sorted_dict[:k]
        
#         top_k_keys = [item[0] for item in top_k_items]
    
#         return top_k_keys
    