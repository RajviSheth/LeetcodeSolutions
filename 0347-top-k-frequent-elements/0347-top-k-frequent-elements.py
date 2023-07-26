class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        dict_count = Counter(nums)
        sorted_dict = sorted(dict_count.items(), key=lambda item:item[1], reverse=True)
        
        top_k_items = sorted_dict[:k]
        
        top_k_keys = [item[0] for item in top_k_items]
    
        return top_k_keys