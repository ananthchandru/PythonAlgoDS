class WordPattern:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        t = s.split()
        mapP, mapT = {}, {}

        for i in range(len(pattern)):
            if (pattern[i] in mapP and t[i] != mapP[pattern[i]]) or (t[i] in mapT and pattern[i] != mapT[t[i]]):
                return False
            mapP[pattern[i]] = t[i]
            mapT[t[i]] = pattern[i]
        return True


obj = WordPattern()
print(obj.wordPattern("abba", "dog cat cat dog"))
print(obj.wordPattern("abba", "dog cat cat fish"))