import collections

class ValidAnagram:
    def isValidAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        countS, countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT

obj = ValidAnagram()
print(obj.isValidAnagram("level", "llvee"))