import heapq
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def solve(self, lists: List[ListNode]) -> ListNode:
        q, h = len(lists), []
        for i in range(q):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i, lists[i]))

        head = ListNode(0)
        res = head
        while h:
            i, n = heapq.heappop(h)[1:]
            res.next = n
            res = res.next
            if n.next:
                heapq.heappush(h, (n.next.val, i, n.next))

        return head.next

    def printListNode(self, recv):
        while recv:
            print('recv.val:', recv.val)
            recv = recv.next

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(7)

    recv = Solution().solve([l1, l2, l3])
    Solution().printListNode(recv)


