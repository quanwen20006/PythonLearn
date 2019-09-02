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

# reduce的使用.函数的参数必须多传一个
# 对sequence中的item顺序迭代调用function
tempY = reduce(lambda d, y: d*2, tempX, 10)
print('reduce: ', tempY)


# filter
tempA = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tempZ = filter(lambda x: x % 2 == 1, tempA)
print(list(tempZ))