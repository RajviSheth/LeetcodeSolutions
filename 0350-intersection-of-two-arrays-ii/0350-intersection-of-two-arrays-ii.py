class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = collections.Counter(nums1)
        res = []

        for num in nums2:
            if counts[num] > 0:
                res.append(num)
                # res += num,
                counts[num] -= 1

        return res
#         aar_1 = [0] * 1000
#         arr_2 = [0] * 1000
        
#         for value in nums1:
#             if arr_1[value] != 0:
#                 arr_1[value] += 1
#             else:
#                 arr_1[value] = 1
                
#         for value in nums2:
#             if arr_2[value] != 0:
#                 arr_2[value] += 1
#             else:
#                 arr_2[value] = 1
                
#         for idx in range(1000):
#             if arr_1[idx] 
        
#         hashmap = {}
#         hashmap_2 = {}
#         for idx in range(max(len(nums1), len(nums2))):
#             if nums1[idx]:
#                 if nums1[idx] in hashmap:
#                     hashmap[nums1[idx]] +=1
#                 else:
#                     hashmap[nums1[idx]] = 1
#             if nums2[idx]:
#                 if nums2[idx] in hashmap_2:
#                     hashmap_2[nums2[idx]] +=1
#                 else:
#                     hashmap_2[nums2[idx]] = 1
                    
            
            
            
        