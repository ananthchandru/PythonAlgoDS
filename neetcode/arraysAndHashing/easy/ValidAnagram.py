import collections

class ValidAnagram:
    #O(N) & O(N) space
    def isValidAnagram1(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        countS, countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT
        
    #O(N) & O(N) space
    def isValidAnagram2(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count = [0] *26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for i in count:
            if i!= 0:
                return False
        return True
    
    #O(N log N) as sorting is involved and O(1) space   
    def isValidAnagram3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s) #returns list of char
        t = sorted(t) #returns list of char
        return s == t
        

obj = ValidAnagram()
print(obj.isValidAnagram1("level", "llvee"))
print(obj.isValidAnagram1("level", "llvev"))
print(obj.isValidAnagram2("level", "llvee"))
print(obj.isValidAnagram2("level", "llvev"))
print(obj.isValidAnagram3("level", "llvee"))
print(obj.isValidAnagram3("level", "llvev"))
