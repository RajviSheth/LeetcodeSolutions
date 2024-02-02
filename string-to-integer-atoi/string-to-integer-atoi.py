class Solution:
    def myAtoi(self, s: str) -> int:
        idx = 0
        sign = 1
        result = 0
        n = len(s)
        
        INT_MAX = pow(2, 31) -1
        INT_MIN = -pow(2, 31)        
        while idx < n and s[idx] == ' ':
            idx += 1
        
        if idx < n and s[idx] == '+':
            sign = 1
            idx += 1
        elif idx < n and s[idx] == '-':
            sign = -1
            idx += 1
            
        while idx < n and s[idx].isdigit():
            digit = int(s[idx])
            
            if (result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            idx += 1
        return result * sign
        