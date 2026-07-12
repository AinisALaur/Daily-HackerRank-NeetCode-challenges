class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        substr = []

        def backtrack(closed, opened):
            if closed + opened == 2 * n:
                res.append("".join(substr))
                return
            
            if closed < opened:
                substr.append(')')
                backtrack(closed + 1, opened)
                substr.pop()

            if opened < n:
                substr.append('(')
                backtrack(closed, opened + 1)
                substr.pop()

        backtrack(0, 0)
        return res