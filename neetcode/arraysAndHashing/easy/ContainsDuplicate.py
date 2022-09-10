class ContainsDuplicate:
    def containsDuplicate(self, nums:[int])->bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return False
            hashset.add(i)
        return True

obj = ContainsDuplicate()
print(obj.containsDuplicate([1,42,222,222,23]))
print(obj.containsDuplicate([1,42,222,212,23]))