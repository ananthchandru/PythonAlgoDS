class NextGreaterElement:
    #O(n*m)
    def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
        hashMap = {v: i for i, v in enumerate(nums1)}
        res = [-1] * len(nums1)
        for i in range(len(nums2)):
            if nums2[i] not in hashMap:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    res[hashMap[nums2[i]]] = nums2[j]
                    break
        return res

    # O(n+m)
    def nextGreaterElement1(self, nums1: [int], nums2: [int]) -> [int]:
        hashMap = {v: i for i, v in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            while stack and nums2[i]>stack[-1]:
                val = stack.pop()
                res[hashMap[val]] = nums2[i]

            if nums2[i] in hashMap:
                stack.append(nums2[i])
        return res


obj = NextGreaterElement()
print(obj.nextGreaterElement1([4, 1, 2], [1, 3, 4, 2]))
print(obj.nextGreaterElement1([2, 4], [1, 2, 3, 4]))