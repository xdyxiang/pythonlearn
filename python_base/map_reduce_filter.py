# a = lambda x: x + 1
# print([a(x) for x in range(10)])

def f(x):
    x = x + 1
    return x 
# map  把一个可迭代的序列在一个方法依次执行上
result = map(f,[1,2,3])
print(result)
print(type(result))
print(list(result))


# reduce  把第一步的结果带入第二步，用于在列表上执行某些计算并返回结果
# 计算0到100的和
from functools import reduce
result = reduce(lambda x,y:x+y, range(101))
print(type(result))
print(result)


def add(a,b):
    return a+b
result2 = reduce(add, range(101))


# filter  该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
# 过滤列表中为大写字母的
l = ["a","A","b","c","C"]

def fun(l):
    for i in l:
        if i.isupper():
            return True

filtered = filter(fun, l)
print(type(filtered))
newlist = list(filtered)
print(newlist)

# 过滤重复的值
l2 = [1,1,2,3,"a","a","b","c"]
l22 = {}.fromkeys(l2)
print(l22.keys())
print(list(l22.keys()))

l3 = [4,5,5,6,1,2,2,1,2,1,3,7]
list1 = list(set(l3))
print(list1)
l3.sort()
print(l3)