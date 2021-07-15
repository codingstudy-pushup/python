class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def solve(self, head):
        # O(n) Time / O(1) Space
        prev = None
        cur = head
        while cur:
            tmp_next = cur.next
            cur.next = prev
            prev = cur
            cur = tmp_next
        return prev

    def printListNode(self, recv):
        while recv :
            print('recv.val:', recv.val)
            recv = recv.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    recv = Solution().solve(head)
    Solution().printListNode(recv)
