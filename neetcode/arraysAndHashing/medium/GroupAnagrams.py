import collections

class GroupAnagrams:
    def groupanagrams(self, strs: [str]) -> [[str]]:
        res = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch)-ord('a')] +=1
            res[tuple(count)].append(s)
        return res.values()

obj = GroupAnagrams()
print(obj.groupanagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
