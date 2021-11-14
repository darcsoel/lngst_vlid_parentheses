class Solution:
    def longestValidParentheses(self, input_string: str) -> int:
        if not input_string:
            return 0

        stack = [-1]
        max_len = 0

        for index, char in enumerate(input_string):
            if char == "(":
                stack.append(index)
            elif char == ")" and stack:
                stack.pop()

            if not stack:
                stack.append(index)

            if stack and index - stack[-1] > max_len:
                max_len = index - stack[-1]

        return max_len
