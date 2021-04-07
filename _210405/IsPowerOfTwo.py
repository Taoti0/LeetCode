"""
题目描述：
    给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
示例：
    输入: 1
    输出: true
    解释: 20 = 1

    输入: 16
    输出: true
    解释: 24 = 16
"""


def way_one(n: int) -> bool:
    if n == 0:
        return False
    return n & (n - 1) == 0


def way_two(n: int) -> bool:
    if n == 0:
        return False
    return n & (-n) == n
