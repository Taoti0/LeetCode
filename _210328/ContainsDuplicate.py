"""
 题目描述：
    给定一个整数数组，判断是否存在重复元素。
    如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false
 示例：
    输入: [1,2,3,1]
    输出: true
"""


# 自想办法（超时）
def way_one(nums):
    for i in range(0, len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j] == nums[i]:
                return True
    return False


def way_two(nums):
    # set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。(哈希表）
    return len(set(nums)) != len(nums)