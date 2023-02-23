class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []
        for c in s:
            if c == '#':
                stack1.pop()
            else:
                stack1.append(c)
        
        for c in t:
            if c == '#':
                stack2.pop()
            else:
                stack2.append(c)
        
        if stack1 == stack2:
            return True
        return False