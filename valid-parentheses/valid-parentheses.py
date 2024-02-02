class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"}":"{", ")":"(", "]":"["}
        
        for value in s:
            if value in brackets:
                if stack:
                    top_element = stack.pop()
                    if top_element != brackets[value]:
                        return False
                else:
                    return False
            else:
                stack.append(value)
            
        return not stack
                