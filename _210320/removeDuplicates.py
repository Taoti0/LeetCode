"""
  题目描述：
    给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素只出现一次 ，返回删除后数组的新长度。
    不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

"""


# 自想办法
def way_one(nums):
    j = 1
    i = 0
    while (j < len(nums)):
        if nums[j] == nums[i]:
            nums.pop(j)
        else:
            i += 1
            j += 1
    return len(nums)


# 官方（双指针）
def way_two(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


nums = [1,2,2,4]
print(way_one(nums))