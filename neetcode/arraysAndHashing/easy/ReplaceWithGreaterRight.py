class ReplaceWithGreaterRight:
    def replace(self, nums:[int])->[int]:
        maxR = -1
        #end of for range will not be included, so use -1 instead of 0
        for i in range(len(nums)-1,-1,-1):
            temp = nums[i]
            nums[i] = maxR
            maxR = max(maxR,temp)
            
        return nums

    def replaceElements(self, arr: [int]) -> [int]:
        maxNum = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], maxNum = maxNum, max(maxNum, arr[i])
        return arr
        
obj = ReplaceWithGreaterRight()
print(obj.replace([17,18,5,4,6,1]))
print(obj.replaceElements([17,18,5,4,6,1]))
