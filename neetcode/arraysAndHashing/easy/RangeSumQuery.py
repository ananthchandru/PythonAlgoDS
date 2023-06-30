class RangeSumQuery:

    def __init__(self, nums: [int]):
        self.arr = []
        sum = 0
        for n in nums:
            sum += n
            self.arr.append(sum)


    def sumRange(self, left: int, right: int) -> int:
        leftArr = self.arr[left - 1] if left > 0 else 0
        return self.arr[right] - leftArr

obj = RangeSumQuery([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))