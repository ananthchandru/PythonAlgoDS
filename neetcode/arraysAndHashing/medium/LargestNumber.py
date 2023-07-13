import functools

class Solution:

    def largestNumber(self, nums:[int])-> str:

        for i,v in enumerate(nums):
            nums[i] = str(v)

        def comparator(n1, n2):
            if n1+n2 > n2+n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key = functools.cmp_to_key(comparator))

        return str(int("".join(nums))) # int conversion is to handle [0,0,0] -> 000 scenario

obj = Solution()
print(obj.largestNumber([10,2]))
print(obj.largestNumber([3,30,34,5,9]))
print(obj.largestNumber([0,0,0]))