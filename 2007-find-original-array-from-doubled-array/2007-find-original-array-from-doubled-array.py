class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        original = []
        changed.sort()
        counter = Counter(changed)
        print(counter)    
        
        for x in changed:
            if counter[x] == 0:
                continue
            if counter[2*x] == 0:
                return []
            counter[x] -= 1
            counter[2*x] -= 1
            original.append(x)
            
        return original if len(original) * 2 == len(changed) else []
        