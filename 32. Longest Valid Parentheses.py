class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:  # s[i] == ')'
                stack.pop()
                if stack:
                    # Calculate length of current valid substring
                    max_length = max(max_length, i - stack[-1])
                else:
                    # Push current index as a new base
                    stack.append(i)

        return max_length
