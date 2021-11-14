from main import Solution


def test_1():
    s = "(()"
    c = Solution().longestValidParentheses(s)
    assert c == 2


def test_2():
    s = ")()())"
    c = Solution().longestValidParentheses(s)
    assert c == 4


def test_3():
    s = "()(()"
    c = Solution().longestValidParentheses(s)
    assert c == 2


def test_4():
    s = "()(())"
    c = Solution().longestValidParentheses(s)
    assert c == 6


def test_5():
    s = "()(())"
    c = Solution().longestValidParentheses(s)
    assert c == 6


def test_6():
    s = ""
    c = Solution().longestValidParentheses(s)
    assert c == 0


def test_7():
    s = "())((())"
    c = Solution().longestValidParentheses(s)
    assert c == 4


def test_8():
    s = ")(()(()(((())(((((()()))((((()()(()()())())())()))()()()())(())()()(((()))))()((()))(((())()((()()())((())))(())))())((()())()()((()((())))))((()(((((()((()))(()()(())))((()))()))())"
    c = Solution().longestValidParentheses(s)
    assert c == 132
