import collections

class GroupAnagrams:
    def groupanagrams(self, strs: [str]) -> [[str]]:
        res = collections.defaultdict(list)
        #https://www.geeksforgeeks.org/defaultdict-in-python/

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch)-ord('a')] +=1
            res[tuple(count)].append(s)
        return res.values()

    def groupanagrams1(self, strs: [str]) -> [[str]]:
        res = collections.defaultdict(list)
        for str in strs:
            res[tuple(sorted(str))].append(str)

        return res.values()

obj = GroupAnagrams()
print(obj.groupanagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
