"""
 题目描述：
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""


# 官方方法（贪心算法）
def way_one(nums) -> int:
    temp = nums[0]
    max_ = temp
    for i in range(1, len(nums)):
        if temp > 0:
            temp += nums[i]
            max_ = max(max_, temp)
        else:
            temp = nums[i]
            max_ = max(max_, temp)
    return max_


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(way_one(nums))