class SubArraySumEqualsK:
    def subArraySum(self, nums:[int], k:int)->int:
        sum = 0
        count = 0
        hashMap = {0:1}
        for i in range(len(nums)):
            sum += nums[i]
            if sum-k in hashMap:
                count += hashMap[sum-k]
            hashMap[sum] = 1 + hashMap.get(sum, 0)
        return count

obj = SubArraySumEqualsK()
print(obj.subArraySum([1,2,3], 3))
print(obj.subArraySum([-1,1,1], 0))
print(obj.subArraySum([-1,0,1], 0))
print(obj.subArraySum([1,-1,0], 0))
print(obj.subArraySum([], 0))