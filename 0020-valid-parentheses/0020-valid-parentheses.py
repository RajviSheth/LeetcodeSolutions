class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_values = {")":"(", "]":"[", "}": "{"}
        for char in s:
            if char in dict_values:
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = '#'
                if dict_values[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
        