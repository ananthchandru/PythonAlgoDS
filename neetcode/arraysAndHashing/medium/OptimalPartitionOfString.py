class OptimalPartitionOfString:
    def optimalPartition(self, s: str)->int:
        res = 0
        hashSet = set()
        for i in\
                range(len(s)):
            if s[i] in hashSet:
                res +=1
                hashSet = set()
            hashSet.add(s[i])
            #to handle last substring
            if i==len(s)-1 and s[i] in hashSet:
                res+=1

        return res #the +1 is if the last character is taken as a partition
obj = OptimalPartitionOfString()
print(obj.optimalPartition("abacaba"))