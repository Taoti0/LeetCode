"""
 题目描述：
    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
    每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    注意：给定 n 是一个正整数。
"""


def way_one(self, n: int) -> int:
    a = b = 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b