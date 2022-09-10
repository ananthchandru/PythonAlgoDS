class TwoSum:
    def twoSum(self, nums:[int], target: int) -> [int]:
        resMap = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in resMap:
                return [i, resMap[diff]]
            resMap[val] = i

obj = TwoSum()
print(obj.twoSum([1,3,5,6], 7))
print(obj.twoSum([1,3,5,6], 2))