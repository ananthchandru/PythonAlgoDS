from collections import Counter


class MaxNumberOfBalloons:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText, countBalloon = {}, {}

        for ch in text:
            countText[ch] = 1 + countText.get(ch, 0)

        for ch in "balloon":
            countBalloon[ch] = 1 + countBalloon.get(ch, 0)

        res = len(text)  # or float("inf")
        for i in countBalloon:
            res = min(res, countText.get(i, 0) // countBalloon[i])
        return res


obj = MaxNumberOfBalloons()
print(obj.maxNumberOfBalloons("nlaebolko"))
print(obj.maxNumberOfBalloons("loonbalxballpoon"))
print(obj.maxNumberOfBalloons("leetcode"))