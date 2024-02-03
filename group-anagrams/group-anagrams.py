class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            track[tuple(count)].append(s)
            
        return track.values()
        
        
#         for value in strs:
#             s_val = ''.join(sorted(value))
#             print(s_val)
#             if s_val in track:
#                 track[s_val].append(value)
#             else:
#                 track[s_val] = [value]
                
#         return track.values()
                