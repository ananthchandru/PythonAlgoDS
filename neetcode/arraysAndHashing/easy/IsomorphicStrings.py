class IsomorphicStrings:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS, mapT = {}, {}

        for i in range(len(s)):
            if (s[i] in mapS and t[i] != mapS[s[i]]) or (t[i] in mapT and s[i] != mapT[t[i]]):
                return False
            mapS[s[i]] = t[i]
            mapT[t[i]] = s[i]
        return True

    def isIsomorphic1(self, s: str, t: str) -> bool:
        mapS, mapT = {}, {}

        for c1, c2 in zip(s, t):
            if (c1 in mapS and mapS[c1] != c2) or (c2 in mapT and mapT[c2] != c1):
                return False
            mapS[c1] = c2
            mapT[c2] = c1

        return True


obj = IsomorphicStrings()
print(obj.isIsomorphic("egg", "add"))
print(obj.isIsomorphic("foo", "bar"))
print(obj.isIsomorphic("paper", "title"))

print(obj.isIsomorphic1("egg", "add"))
print(obj.isIsomorphic1("foo", "bar"))
print(obj.isIsomorphic1("paper", "title"))