class Solution:
    def minSwaps(self, s: str) -> int:
        extraClose, maxClose = 0, 0

        for c in s:
            if c == "]":
                extraClose += 1
            else:
                extraClose -= 1
            maxClose = max(maxClose, extraClose)
        return (maxClose + 1) // 2

obj = Solution()
print(obj.minSwaps("][][")) #resulting string "[[]]"
print(obj.minSwaps("]]][[[")) #resulting string "[[][]]"
print(obj.minSwaps("[]")) #string already balanced