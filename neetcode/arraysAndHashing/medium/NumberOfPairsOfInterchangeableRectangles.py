class Solution:
    def interchangeableRectangles(self, rectangles: [[int]]) -> int:
        count = 0
        hashMap = {}
        for rect in rectangles:
            hashMap[rect[1]/rect[0]] = 1 + hashMap.get(rect[1]/rect[0],0)
        for v in hashMap.values():
            count += v*(v-1)//2
        return count

obj = Solution()
print(obj.interchangeableRectangles([[4,8],[3,6],[10,20],[15,30]]))
print(obj.interchangeableRectangles([[4,5],[7,8]]))