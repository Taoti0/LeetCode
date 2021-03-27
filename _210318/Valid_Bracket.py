"""
 题目描述：
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
    有效字符串需满足：
        1、左括号必须用相同类型的右括号闭合。
        2、左括号必须以正确的顺序闭合。
"""


# 定义一个栈（顺序栈）
class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):  # 判断是否为空
        return bool(self.stack)     # False为空，true不为空

    def push(self, value):  # 入栈
        self.stack.append(value)

    def pop(self):  # 出栈
        if self.stack:
            return self.stack.pop()
        else:
            raise LookupError('stack is empty')

    def size(self):
        return len(self.stack)

    def peek(self):
        if self.stack:
            return self.stack[self.size() - 1]
        else:
            raise LookupError('stack is empty')

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            raise LookupError('stack is empty')


# 自想方法
def way_one(s: str):
    braStack = Stack()
    braDict = {'(': ')', '{': '}', '[': ']'}  # 定义一个括号键值对字典
    for item in s:
        if item == '(' or item == '{' or item == '[':
            braStack.push(item)
        else:
            if not braStack.isEmpty():
                return False
            leftBra = braStack.pop()
            if item != braDict[leftBra]:
                return False
    # 栈中需无元素
    if not braStack.isEmpty():
        return True
    else:
        return False

