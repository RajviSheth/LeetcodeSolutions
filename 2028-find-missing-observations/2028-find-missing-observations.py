class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        length = len(rolls) + n
        
        missing_sum = (mean * length) - sum(rolls)
        
        if missing_sum < n or missing_sum > n * 6:
            return []
        res = []
        
        while missing_sum:
            dice = min(missing_sum - n + 1, 6)
            res.append(dice)
            n -= 1
            missing_sum -= dice
        return res