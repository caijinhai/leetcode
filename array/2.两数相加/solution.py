# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i = 0
        sum = 0
        while l1:
            sum = sum + pow(10, i) * l1.val
            l1 = l1.next
            i += 1
        j = 0
        while l2:
            sum = sum + pow(10, j) * l2.val
            l2 = l2.next
            j += 1
        
        arr = []
        while sum >= 10:
            arr.append(sum % 10)
            sum = int(sum / 10)
        arr.append(sum)
        arr.reverse()

        res = None
        for item in arr:
            if not res:
                res = ListNode(item)
            else:
                node = ListNode(item)
                node.next = res
                res = node
        
        return res


class Solution2(object):

    def addTwoNumbers(self, l1, l2):
        dummyHead = ListNode(0)
        current = dummyHead
        p = l1
        q = l2
        carry = 0
        while p is not None and q is not None:
            val1 = 0
            val2 = 0
            if p.val:
                val1 = p.val
            if q.val:
                val2 = q.val
            sum = carry + val1 + val2
            yu = sum % 10
            carry = int(sum / 10)
            current.next = ListNode(yu)
            current = current.next
            p = p.next
            q = q.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummyHead.next



if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    res = (Solution2().addTwoNumbers(l1, l2))
    # 2->4->3 + 5->6->4 == 342 + 465 = 807, 7->0->8
    print(res.val, res.next.val, res.next.next.val)