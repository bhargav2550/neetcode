class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(a,b):
            prev = None
            curr = a
            while curr != b:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        
        if not head:
            return None
        a = b = head
        for _ in range(k):
            if not b:
                return a
            b = b.next
        new_head = reverse(a,b)
        a.next = self.reverseKGroup(b,k)
        return new_head
        