class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_map = {')':'(', ']' : '[', '}' : '{'}
        
        for char in s:
            if char in dict_map:
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = '#'
                if dict_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack
        
        
        
            
        