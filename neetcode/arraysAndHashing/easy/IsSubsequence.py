class Subsequence:
    def isSubsequence(self, str1: str, str2:str)->[int]:
        i,j=0,0
        while i<len(str1) and j<len(str2):
           if(str1[i]==str2[j]):
               i+=1
           j+=1
    
        return i == len(str1)
        
obj = Subsequence()
print(obj.isSubsequence("abc","ahbgdc"))
print(obj.isSubsequence("acb","ahbgdc"))
