"""
题目描述：
    给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
示例：
    输入："Let's take LeetCode contest"
    输出："s'teL ekat edoCteeL tsetnoc"
"""


# 自想办法 （耗时长 110 - 140 ms )
def way_one(s: str) -> str:
    s = s + " "
    stack = []
    re = ""
    for item in s:
        if item != " ":
            stack.append(item)
        else:
            for i in range(len(stack)):
                re = re + stack[-1 - i]
            re = re + " "
            stack = []
    return re[:-1]


# 方法二 （翻转切片）
def way_two(s):
    # return " ".join(word[::-1] for word in s.split(" "))
    return " ".join(s.split(" ")[::-1])[::-1]
