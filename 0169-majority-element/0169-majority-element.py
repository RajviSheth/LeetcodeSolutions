class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        track = {}
        for num in nums:
            if num in track:
                track[num] += 1
            else:
                track[num] = 1
        for key, value in track.items():
            if value >= len(nums) / 2:
                return key

        