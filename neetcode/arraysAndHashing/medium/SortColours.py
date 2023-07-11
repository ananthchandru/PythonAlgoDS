class SortColours:
    def sortColors(self, nums: [int]) -> None:
        #we use 3 pointers
        i, j, mid = 0, len(nums)-1, 0
        while mid<=j:
            if nums[mid]==0:
                nums[i], nums[mid] = nums[mid], nums[i]
                i+=1
                mid+=1
            elif nums[mid]==2:
                nums[j], nums[mid] = nums[mid], nums[j]
                j-=1
            else:#nums[mid]==1:
                mid+=1
        return nums

obj = SortColours()
print(obj.sortColors([2,0,2,1,1,0]))
print(obj.sortColors([]))
print(obj.sortColors([2,0,1]))