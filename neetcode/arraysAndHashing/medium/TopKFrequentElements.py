class TopKFrequentElements:
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

obj = TopKFrequentElements()
print(obj.freqElements([1,1,1,2,2,2,3,3,4], 2))