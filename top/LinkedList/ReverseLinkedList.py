class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def solve(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def printListNode(self, recv):
        while recv :
            print('recv.val:', recv.val)
            recv = recv.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    Solution().printListNode(head)
    recv = Solution().solve(head)
    Solution().printListNode(recv)
