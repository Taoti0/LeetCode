"""
题目描述：
    反转一个单链表。
示例：
    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def way_one(head: ListNode) -> ListNode:    # 迭代
    cur, pre = head, None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre
