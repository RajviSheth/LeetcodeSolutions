class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1
        count = 9
        start = 1
        # n=13
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
        
        
        # n = 4
        # n / length
        # find out the exact number
        start += (n - 1) // length
        # find out the exact digit
        return int(str(start)[(n - 1) % length])
