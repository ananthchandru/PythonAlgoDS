class Solution:

    def zeroFilledSubarray(self, nums: [int]) -> int:
        count, res = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                count = 0
            #Add individual counts + total count (similar to n*(n+1)/2)
            res += count
        return res

    def zeroFilledSubarray1(self, nums: [int]) -> int:
        count, subArray = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            if nums[i] != 0 and i < len(nums) - 1:
                subArray += (count * (count + 1)) // 2
                count = 0
        subArray += (count * (count + 1)) // 2
        return subArray

obj = Solution()
print(obj.zeroFilledSubarray([1,3,0,0,2,0,0,4]))
print(obj.zeroFilledSubarray([0,0,0,2,0,0]))
print(obj.zeroFilledSubarray([2,10,2019]))
print(obj.zeroFilledSubarray1([1,3,0,0,2,0,0,4]))
print(obj.zeroFilledSubarray1([0,0,0,2,0,0]))
print(obj.zeroFilledSubarray1([2,10,2019]))