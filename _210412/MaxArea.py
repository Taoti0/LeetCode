"""
题目描述：
    给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
    在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
    找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
示例：
    输入：[1,8,6,2,5,4,8,3,7]
    输出：49
    解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
    图例：https://leetcode-cn.com/problems/container-with-most-water/
"""


# 方法一 双指针
def way_one(height) -> int:
    l, r = 0, len(height) - 1
    ans = 0
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        ans = max(ans, area)
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return ans


# 方法二 （和一思路一致，但是耗时更少）
def way_two(height) -> int:
    l, r, ans = 0, len(height) - 1, 0
    while l < r:
        if height[l] < height[r]:
            ans = max(ans, height[l] * (r - l))
            l += 1
        else:
            ans = max(ans, height[r] * (r - l))
            r -= 1
    return ans
