import string

class Solution:

    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0
        chars = set(s)
        for char in chars:
            first, last = s.find(char), s.rfind(char)
            count += len(set(s[first + 1:last]))
        return count


    def countPalindromicSubsequence1(self, s: str) -> int:
        res = 0
        charSet = set(s)
        for ch in charSet:
            hashset = set()
            i,j=0,len(s)-1
            while(i<len(s) and s[i]!=ch):
                i+=1
            while (j>0 and s[j]!=ch):
                j-=1
            if i<len(s) and j>0 and i<j:
                for k in range(i+1, j):
                    hashset.add(s[k])
            res += len(hashset)
        return res



obj = Solution()
print(obj.countPalindromicSubsequence("aabcca"))
print(obj.countPalindromicSubsequence("adc"))
print(obj.countPalindromicSubsequence("bbcbaba"))
print(obj.countPalindromicSubsequence1("aabcca"))
print(obj.countPalindromicSubsequence1("adc"))
print(obj.countPalindromicSubsequence1("bbcbaba"))