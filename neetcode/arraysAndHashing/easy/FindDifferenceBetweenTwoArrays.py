class FindDifferenceBetweenTwoArrays:
    def findDiff(self, nums1:[int], nums2:[int])->[[int]]:
        set1, set2 = set(nums1), set(nums2)
        res1, res2 = [],[]
        for n in set1:
            if n not in set2:
                res1.append(n)
        for n in set2:
            if n not in set1:
                res2.append(n)
        return [res1,res2]

obj = FindDifferenceBetweenTwoArrays()
print(obj.findDiff([1,2,3],[2,4,6]))
print(obj.findDiff([1,2,3,3],[1,1,2,2]))