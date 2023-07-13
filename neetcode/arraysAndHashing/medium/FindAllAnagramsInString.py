class Solution:

    def findAnagrams(self, s: str, p: str) -> [int]:
        if len(p) > len(s): return []
        sMap, pMap = {}, {}
        res = []
        for i in range(len(p)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            pMap[p[i]] = 1 + pMap.get(p[i], 0)

        if sMap == pMap:
            res.append(0)

        k = 0
        for i in range(len(p), len(s)):
            sMap[s[k]] -= 1
            if sMap[s[k]] == 0:
                sMap.pop(s[k])
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            k += 1
            if sMap == pMap:
                res.append(k)
        return res

    def findAnagrams1(self, s: str, p: str) -> [int]:

            startIndex = 0
            pMap, sMap = {}, {}
            res = []

            for char in p:
                pMap[char] = 1 + pMap.get(char, 0)

            for i in range(len(s)):
                sMap[s[i]] = 1 + sMap.get(s[i], 0)

                if i >= len(p) - 1:
                    if sMap == pMap:
                        res.append(startIndex)

                    # If current character is in sMap, remove it and re-update the map.
                    if s[startIndex] in sMap:
                        sMap[s[startIndex]] -= 1
                        if sMap[s[startIndex]] == 0:
                            del sMap[s[startIndex]]
                    startIndex += 1

            return res

obj = Solution()
print(obj.findAnagrams("cbaebabacd", "abc"))
print(obj.findAnagrams("abab", "ab"))

print(obj.findAnagrams1("cbaebabacd", "abc"))
print(obj.findAnagrams1("abab", "ab"))