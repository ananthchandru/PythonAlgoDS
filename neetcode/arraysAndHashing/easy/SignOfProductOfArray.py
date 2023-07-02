class SignOfProductOfArray:
    def findSign(self, nums:[int])->int:
        count = 0
        for n in nums:
            if n==0:
                return 0
            count+=1 if n<0 else 0
        return -1 if count%2 else 1

obj = SignOfProductOfArray()
print(obj.findSign([-1,-2,-3,-4,3,2,1]))
print(obj.findSign([1,5,0,2,-3]))
print(obj.findSign([-1,1,-1,1,-1]))