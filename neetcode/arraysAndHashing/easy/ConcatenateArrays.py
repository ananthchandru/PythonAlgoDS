class ConcatenateArrays:
    def concat1(self, nums: [int])->[int]:
        res = [0] * len(nums)*2
        for i in range(len(nums)):
            res[i] = nums[i]
            res[i+len(nums)] = nums[i]
        return res
        
    def concat2(self, nums: [int])->[int]:
        return nums*2
        
    def concat3(self, nums: [int])->[int]:
        return nums+nums
        
    def concat4(self, nums: [int])->[int]:
        res = []
        for i in range(2):
            for i in nums:
                res.append(i)
        return res
        
        
obj = ConcatenateArrays()
print(obj.concat1([1,2,3]))
print(obj.concat2([1,2,3]))
print(obj.concat3([1,2,3]))
print(obj.concat4([1,2,3]))
