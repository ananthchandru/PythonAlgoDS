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

    def isValidAnagram2(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count = [0] *26
        for i in s:
            count[ord(i) - ord('a')] += 1
        for i in t:
            count[ord(i) - ord('a')] -= 1
        for i in count:
            if i> 0:
                return False
        return True

obj = ValidAnagram()
print(obj.isValidAnagram2("level", "llvee"))