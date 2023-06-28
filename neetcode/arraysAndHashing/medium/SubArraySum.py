class SubArraySum:
    def subarraySum(self, nums:[int], k:int)->int:
                count = 0
                sum = 0
                dic = {}
                dic[0] = 1
                for i in range(len(nums)):
                    sum += nums[i]
                    if sum - k in dic:
                        count += dic[sum - k]
                    dic[sum] = dic.get(sum, 0) + 1
                return count

obj = SubArraySum()
print(obj.subarraySum([1,2,3],3))

        # Time Complexity :
        #     O(N) -> Where N is the size of the array and we are iterating over the array once

        # Space Complexity:
        #     O(N) -> Creating a hashmap/dictionary
