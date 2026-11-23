class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }
        for chr in s:
            if chr in "({[":
                stack.append(chr)
            else:
                if not stack:
                    return False
                top = stack.pop()

                if top != pairs[chr]:
                    return False
        return len(stack) == 0