class Solution:
    def findRepeatedDnaSequences(self, s: str) -> [str]:
        res, seen = set(), set()
        for i in range(len(s)-9):
            str = s[i:i+10]
            if str in seen:
                res.add(str)
            seen.add(str)
        return res

obj = Solution()
print(obj.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(obj.findRepeatedDnaSequences("AAAAAAAAAAAAA"))