"""
题目描述：
    给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
    你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例：
    输入：[3,2,3]
    输出：3

    输入：[2,2,1,1,1,2,2]
    输出：2
"""

import collections
"""
方法一 ：哈希表
算法思想：
    用一个循环遍历数组 nums 并将数组中的每个元素加入哈希映射中。
    在这之后，我们遍历哈希映射中的所有键值对，返回值最大的键。
    同样也可以在遍历数组 nums 时候使用打擂台的方法，维护最大的值，这样省去了最后对哈希映射的遍历。
补充：
    collections 为 python 的一个高性能容量数据类型，总共包含 9 种数据类型
        namedtuple()    创建命名元组子类的工厂函数
        deque           类似列表(list)的容器，实现了在两端快速添加(append)和弹出(pop)
        ChainMap        类似字典(dict)的容器类，将多个映射集合到一个视图里面
        Counter         字典的子类，提供了可哈希对象的计数功能
        OrderedDict     字典的子类，保存了他们被添加的顺序
        defaultdict     字典的子类，提供了一个工厂函数，为字典查询提供一个默认值
        UserDict        封装了字典对象，简化了字典子类化
        UserList        封装了列表对象，简化了列表子类化
        UserString      封装了列表对象，简化了字符串子类化

"""
def way_one(nums) -> int:
    counts = collections.Counter(nums)
    return max(counts.key(), key=counts.get)


"""
方法二 ： 排序
算法思想：
    如果将数组 nums 中的所有元素按照单调递增或单调递减的顺序排序，那么下标为⌊n/2⌋ 的元素（下标从 0 开始）一定是众数。
"""
def way_two(nums) -> int:
    n = len(nums)
    nums.sort()
    return nums[n // 2]


"""
方法三 ： 摩尔投票法
算法思想：
    数值不相同的两数相互抵消，最后剩下的一定是数量最多的数
    major 用来记录 count 为0是最近的值
"""
def way_three(nums) -> int:
    count = 0
    for item in nums:
        if not count:   # 先判 count 为0 ，执行用时可能会更高（最好效果为 36ms，击败了98.19%的用户）
            major = item
            count = 1
        else:
            count = count + 1 if major == item else count - 1
    return major
