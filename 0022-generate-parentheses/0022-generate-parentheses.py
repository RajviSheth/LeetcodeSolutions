class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # add open paranthesis when open < n
        # add closed parenthesis when close < open
        # stop when close = open = n
        
        stack = []
        res = []
        
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()
                
        backtrack(0, 0)
        return res