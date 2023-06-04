class LongestCommonPrefix:
    def longestPrefix(self, strs: [str])->str:
        res = ""
        for i in range(len(strs[0])):
            for str in strs:
                if(i==len(str) or strs[0][i] != str[i]):
                    return res
            res += strs[0][i]    
        return res
        
        
obj = LongestCommonPrefix()
print(obj.longestPrefix(["flower","flow","flight"]))
print(obj.longestPrefix(["dog","racecar","car"]))
