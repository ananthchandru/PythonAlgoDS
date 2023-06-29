class MajorityElement:
    def majorityElement(self, nums: [int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)

        return res

    def majorityElement1(self, nums: [int]) -> int:
        map = {}
        for n in nums:
            map[n] = 1 + map.get(n, 0)
            if(map.get(n)>len(nums)/2):
                return n
        return -1

obj = MajorityElement()
print(obj.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(obj.majorityElement([3, 2, 3]))
print()
print(obj.majorityElement1([2, 2, 1, 1, 1, 2, 2]))
print(obj.majorityElement1([3, 2, 3]))