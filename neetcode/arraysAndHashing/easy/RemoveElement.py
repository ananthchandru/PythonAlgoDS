class RemoveElement:
    def removeElement(self, nums: [int], val:int)->int:
        
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1  
        return k
        
        
obj = RemoveElement()
print(obj.removeElement([3,2,2,3],3))
print(obj.removeElement([0,1,2,2,3,0,4,2],2))
