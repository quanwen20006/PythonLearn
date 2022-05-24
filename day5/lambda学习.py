'''
    主要是熟悉python的匿名函数，机高阶函数的使用
'''
from functools import reduce

a = [1, 2, 3, 4, 5]
tempxT = lambda a: a**2
print('tempxT: ', tempxT(11))

# 三元表达式
x = 1
y = 2
print("大于" if x > y else "小于")

# map,对sequence中的item依次执行function(item)，将执行结果function(item)组成一个List返回
tempX = [1, 2, 3, 4, 5]
print('map: ', list(map(lambda d: d**2, tempX)))


# reduce(function，iterable[, initializer]，)
# function 需要2个参数，1个用于保存操作结果，另一个是每次迭代的元素
# iterable 待迭代处理的集合
# initializer 初始值，可以没有，相当于 集合 多了一个元素，第一个元素是initializer的值
# 用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果
# 对sequence中的item顺序迭代调用function
tempY = reduce(lambda d, y: d*2, tempX, 10)
print('reduce: ', tempY)


# filter
tempA = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tempZ = filter(lambda x: x % 2 == 1, tempA)
print(list(tempZ))

listT = [1, 2, 3, 4]
t = reduce(lambda x, y: x*2, listT)
print("t: {}".format(t))


def add(a, b):
    return a*2

t1 = reduce(add, listT, 20)
print("t1: {}".format(t1))
