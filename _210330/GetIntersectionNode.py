"""
 题目描述：
    编写一个程序，找到两个单链表相交的起始节点。
 示例：
    输入：listA = [4,1,8,4,5], listB = [5,0,1,8,4,5]
    输出：Reference of the node with value = 8
    输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，
              链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
"""


def way_one(headA,headB):
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a