class FindIndexOfFirstOccurrenceOfString:
    def findIndex(self, haystack:str, needle:str)->int:

        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                j,k = i+1,1
                while(k<len(needle) and haystack[j]==needle[k]):
                    j+=1
                    k+=1
                if k==len(needle):
                    return i
        return -1

    #def KMPLogicPending

obj =  FindIndexOfFirstOccurrenceOfString()
print(obj.findIndex("sabbutsad", "sad"))