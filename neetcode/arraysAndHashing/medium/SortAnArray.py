class SortAnArray:
    def sortArray(self, nums:[int])->[int]:
        self.mergeSort(nums, 0, len(nums)-1)
        return nums

    def mergeSort(self, nums:[int], l:int, r:int)->[int]:
        if l<r:
            mid = l + (r-l)//2
            self.mergeSort(nums, l, mid)
            self.mergeSort(nums, mid+1,r)
            self.merge(nums, l, mid, r)
        return nums

    def merge(self, nums:[int], l:int, mid:int, r:int)->[int]:
        left, right = nums[l:mid+1], nums[mid+1:r+1]
        i,j,k = 0,0,l
        while i<len(left) and j<len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1
        while i<len(left):
            nums[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            nums[k] = right[j]
            j+=1
            k+=1
        return nums

#Another code without additional methods
    def mergeSort1(self, nums)->int:
        if len(nums) > 1:
            mid = len(nums) // 2
            L = nums[:mid]
            R = nums[mid:]

            self.mergeSort1(L)
            self.mergeSort1(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1
            return nums

obj = SortAnArray()
print(obj.sortArray([5,2,3,1]))
print(obj.mergeSort1([5,2,3,1]))