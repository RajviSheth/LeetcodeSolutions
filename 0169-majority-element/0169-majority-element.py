class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        track = {}
        for num in nums:
            track[num] = track.get(num, 0) + 1
        for key, value in track.items():
            if value >= len(nums) / 2:
                return key

        