"""
题目描述：
    给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储一位数字。
    请你将两个数相加，并以相同形式返回一个表示和的链表。
    你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
    输入：l1 = [2,4,3], l2 = [5,6,4]
    输出：[7,0,8]
    解释：342 + 465 = 807.

    输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    输出：[8,9,9,9,0,0,0,1]
    解释：9999999 + 9999 = 10009998
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 自想办法 （耗时 70 - 80 ms，内存 15M左右，和大部分python解法差不多，但是写法不够优美）
def way_one(l1: ListNode, l2: ListNode) -> ListNode:
    l3 = ListNode()
    tmp = l3
    i = 0  # 用来进位
    while l1 or l2:
        num = 0
        if l1:
            l1.val += i
            i = 0
            num += l1.val
            l1 = l1.next
        if l2:
            l2.val += i
            i = 0
            num += l2.val
            l2 = l2.next
        if num >= 10:
            num -= 10
            i = 1
        tmp.next = ListNode(num)
        tmp = tmp.next
    if i:  # 最后一次仍然超过10，需进一位，但此时l1或l2没有了
        tmp.next = ListNode(i)
        tmp = tmp.next
    return l3.next


# 方法二
def way_two(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(l1.val + l2.val)
    cur = head
    while l1.next or l2.next:
        l1 = l1.next if l1.next else ListNode()
        l2 = l2.next if l2.next else ListNode()
        cur.next = ListNode(l1.val + l2.val + cur.val // 10)
        cur.val = cur.val % 10
        cur = cur.next
    if cur.val >= 10:
        cur.next = ListNode(cur.val // 10)
        cur.val = cur.val % 10
    return head