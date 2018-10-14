import heapq


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = list()
        sortedl = ListNode(0)

        #initialize pq
        for i in range(0, len(lists)):
            heapq.heappush(pq, lists[i])

        # go through pq until its empty
        while len(pq) != 0:
            low = heapq.heappop(pq)
            sortedl.next = ListNode(low.val)
            if low.next is not None:
                heapq.heappush(pq, low.next)
        return sortedl


def printLL(n):
    print n.val
    if n.next is not None:
        printLL(n.next)


L1 = ListNode(5)
L1.next = ListNode(10)
L1.next.next = ListNode(15)

L2 = ListNode(6)
L2.next = ListNode(12)
L2.next.next = ListNode(18)

L3 = ListNode(7)
L3.next = ListNode(11)
L3.next.next = ListNode(14)


printLL(Solution().mergeKLists([L1, L2, L3]))