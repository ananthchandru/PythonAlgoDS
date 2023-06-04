class ReplaceWithGreaterRight:
    def replace(self, nums:[int])->[int]:
        maxR = -1
        #end of for range will not be included, so use -1 instead of 0
        for i in range(len(nums)-1,-1,-1):
            temp = nums[i]
            nums[i] = maxR
            maxR = max(maxR,temp)
            
        return nums
        
obj = ReplaceWithGreaterRight()
print(obj.replace([1,2,3,4]))
