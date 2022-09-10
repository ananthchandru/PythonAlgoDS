class ContainsDuplicate:

    def containsDuplicate(self, nums: [int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

obj = ContainsDuplicate()
print(obj.containsDuplicate([1, 42, 222, 222, 23]))
print(obj.containsDuplicate([1, 42, 222, 212, 23]))
