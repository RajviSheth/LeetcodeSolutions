class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        answer = [1] * len(nums)
        answer[0] = 1
        for index in range(1, len(nums)):
            left = left * nums[index - 1]
            answer[index] = left
        for index_1 in reversed(range(len(nums)-1)):
            print(index_1)
            right = right * nums[index_1 + 1]
            answer[index_1] = answer[index_1] * right 
        return answer
