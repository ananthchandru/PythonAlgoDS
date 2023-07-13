class Solution:
    def contSubArray(self, nums:[int], k:int)->bool:
        hashMap = {0:-1} # to handle scenario where nums = [0, 24], K =6

        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            rem = sum%k
            if rem not in hashMap:
                hashMap[rem] = i
            elif i - hashMap[rem] > 1:
                    return True
        return False

obj = Solution()
print(obj.contSubArray([23,2,4,6,7], 6))
print(obj.contSubArray([23,2,6,4,7], 6))
print(obj.contSubArray([23,2,6,4,7], 13))
print(obj.contSubArray([0, 24], 6))
print(obj.contSubArray([24], 6))