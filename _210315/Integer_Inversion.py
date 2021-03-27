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
    # 判断 x 是否为负数,若为负数，i = -1
    if x_1 < 0:
        i = -1
    else:
        i = 1
    x_1 = x_1 * i
    str_x = str(x_1)  # 数组化 x
    while str_x[-1] == 0:
        str_x.pop()  # 最后一位为0，则删除最后一位
    n = 1
    new_x = 0
    for item in str_x:
        new_x = int(item) * n + new_x
        n = n * 10
    # 判断反转后整数是否超过 32 位
    if new_x > 2 ** 31 - 1:
        new_x = 0
    else:
        new_x = new_x * i
    return new_x


# 网友答案（绝了！）
def way_two(x_2: int) -> int:   # 指定参数（x_2）的类型， 函数的返回类型（-> int）， 以及局部变量的类型
    y, res = abs(x_2), 0
    # 如果 x_2 大于0，boundary = (1 << 31) - 1，否则 boundary = 1 << 31
    boundary = (1 << 31) - 1 if x_2 > 0 else 1 << 31
    while y != 0:
        res = res * 10 + y % 10
        if res > boundary:
            return 0    # res 的结果比2^31 − 1（或2^31）大，返回0
        y //= 10
    return res if x_2 > 0 else -res


x = input("请输入一个整数：")
x = int(x)
print(way_one(x))
print(way_two(x))
