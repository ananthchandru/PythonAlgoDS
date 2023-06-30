class FindDisappearedNumbers:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])
            #print(nums)

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res


obj = FindDisappearedNumbers()
print(obj.findDisappearedNumbers([4, 3, 4, 1]))