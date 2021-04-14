"""
题目描述：
    在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
示例：
    输入: [3,2,1,5,6,4] 和 k = 2
    输出: 5

    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
    输出: 4
"""

from typing import List
import heapq


# 方法一 暴力解法
def way_one(nums: List[int], k: int) -> int:
    nums.sort()
    return nums[-k]


# 方法二 快速排序
def way_two(self, nums: List[int], k: int) -> int:
    size = len(nums)
    target = size - k
    left = 0
    right = size - 1
    while True:
        index = self.__partition(nums, left, right)
        if index == target:
            return nums[index]
        elif index < target:
            # 下一轮在 [index + 1, right] 里找
            left = index + 1
        else:
            right = index - 1


#  循环不变量：[left + 1, j] < pivot
#  (j, i) >= pivot
def __partition(self, nums, left, right):
    pivot = nums[left]
    j = left
    for i in range(left + 1, right + 1):
        if nums[i] < pivot:
            j += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[left], nums[j] = nums[j], nums[left]
    return j


# 方法三 优先队列
def way_three(self, nums: List[int], k: int) -> int:
    size = len(nums)
    if k > size:
        raise Exception('程序出错')
    L = []
    for index in range(k):
        # heapq 默认就是小顶堆
        heapq.heappush(L, nums[index])
    for index in range(k, size):
        top = L[0]
        if nums[index] > top:
            # 看一看堆顶的元素，只要比堆顶元素大，就替换堆顶元素
            heapq.heapreplace(L, nums[index])
    # 最后堆顶中的元素就是堆中最小的，整个数组中的第 k 大元素
    return L[0]
