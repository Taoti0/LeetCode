"""
题目描述：
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""
"""


# 自想办法
class Solution(object):
    def longestCommonPrefix(self, strs):
        strsLen = len(strs)
        res =strs[0]
        for i in range(1, strsLen):
            res = self.lcp(res, strs[i])
            if not res:
                break
        return res

    def lcp(self, str1, str2):
        index = 0
        minLen = min(len(str1),len(str2))
        while index < minLen and str1[index] == str2[index]:
            index += 1
        return str1[:index]