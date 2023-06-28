import collections

class TopKFrequentElements:

    # n(log n) : sort the items and iterate and find  k frequent
    # K* log N : heapify
    # O(N) bucket sort: solved in O(N)
    def freqElements(self, nums: [int], k: int) -> [int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    def topKFrequent(self, nums: [int], k: int) -> [int]:

        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        #sort map by values
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        print(type(freq.keys()))

        return None

    def topKFreqShortCode(self, nums:[int], k: int)-> [int]:
        if k==len(nums):
            return nums
        cmap = collections.Counter(nums)
        #print(cmap)

        return sorted(cmap.keys(), key = lambda x:cmap[x], reverse = True)[:k]

obj = TopKFrequentElements()
print(obj.freqElements([4,4,4,3,3,3,1,1,2], 2))
print(obj.topKFrequent([4,4,4,3,3,3,1,1,2], 2))
print(obj.topKFreqShortCode([4,4,4,3,3,3,1,1,2], 2))