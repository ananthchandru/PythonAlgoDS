#https://leetcode.com/problems/design-hashmap/solutions/1097755/js-python-java-c-updated-hash-array-solutions-w-explanation/

class ListNode:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next

class HashMap:
    def __init__(self, size:int):
        self.map = [ListNode for i in range(10)]

    def hashCode(self, key:int)->int:
        return key % len(self.map)

    def put(self, key, value):
        cur = self.map[self.hashCode(key)]
        print(cur)
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = ListNode(key,value)

    def get(self, key:int)->int:
        cur = self.map[self.hashCode(key)].next #as first node is a dummy node
        while cur:
            if cur.key==key:
                return cur.value
            cur = cur.next
        return -1

    def remove(self, key:int):
        cur = self.map[self.hashCode(key)].next #as first node is a dummy node
        while cur and cur.next:
            if cur.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

obj = HashMap(5)
obj.put(1,100)
print(obj)
