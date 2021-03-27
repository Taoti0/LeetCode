"""
题目描述：
    给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
    如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
    假设环境不允许存储 64 位整数（有符号或无符号）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
"""


# 自想答案
def way_one(x_1):
    x_1 = str(x_1)
    n = len(x_1)
    for i in range(0, n // 2):
        if x_1[i] == x_1[n - i - 1]:
            i += 1
        else:
            return False
    return True


# 自想答案，利用_210315的方法二
def way_one(x_2):
    y, res = abs(x_2), 0
    while y != 0:
        res = res * 10 + y % 10
        y //= 10
    if x_2 == res:
        return True
    return False
