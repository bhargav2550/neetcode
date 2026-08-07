class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.s = [ListNode(0,0) for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        index = key % len(self.s)
        curr = self.s[index]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key,value)

    def remove(self, key: int) -> None:
        index = key % len(self.s)
        curr = self.s[index]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def get(self, key: int) -> int:
        index = key % len(self.s)
        curr = self.s[index]
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)