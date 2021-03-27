""""
 题目描述：
    将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的
    示例
        输入：l1 = [1, 2, 4], l2 = [1, 3, 4]
        输出：[1, 1, 2, 3, 4, 4]
"""
import math

# 定义一个Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 定义顺序链表
class LinkList:
    def __init__(self):
        self.head = None

    def creatLink(self, data):
        if not data:
            res = "your list is None"
            return ListNode(res)
        self.head = ListNode(data[0])
        res = self.head
        p = self.head
        for item in data[1:]:
            node = ListNode(item)
            p.next = node
            p = p.next
        return res

    def printLink(self, link):
        if not link: return "[]"
        copyLink = link
        res = []
        while copyLink:
            res.append(copyLink.val)
            copyLink = copyLink.next
        return res

    '''
    def deleteLink(self, link, nodePosition):
        copyLink = link
        res = self.printLink(copyLink)
        return res
    '''

    def releaseLink(self):
        self.head = None    # 应该有问题


# 方法一
def way_one(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1: return l2  # 终止条件，直到两个链表都空
    if not l2: return l1
    if l1.val <= l2.val:  # 递归调用
        l1.next = way_one(l1.next, l2)
        return l1
    else:
        l2.next = way_one(l1, l2.next)
        return l2


# 方法二
def way_two(l1: ListNode, l2: ListNode) -> ListNode:
    prehead = ListNode(-1)
    prev = prehead          # 创建一个空链接
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
    # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
    prev.next = l1 if l1 is not None else l2
    return prehead.next


lst1 = [1, 3, 5, 5]
lst2 = [1, 2, 4]
lst3 = []
l1 = LinkList().creatLink(lst1)
l2 = LinkList().creatLink(lst2)
l3 = LinkList().creatLink(lst3)
#l4 = (LinkList().printLink(l3))

s = [[3, 2],[4],[3,2]]
info = []
x1 = 5/14
x2 = 4/14
x3 = 5/14
x = [x1,x2,x3]
for item in s:
    n = 0
    for i in item:
        p = i / sum(item)
        n = n + (-p*math.log(p, 2))
    info.append(n)

su = 0
for j in range(len(info)):
    su = info[j] * x[j] + su
print(su)



