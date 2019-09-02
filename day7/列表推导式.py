'''
列表推导式
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [i**3 for i in a]
print(b)

# 如果i大于5，再进行列表推导式
c = [i**3 for i in a if i > 5]
print(c)


# 如果针对set集合进行列表推导式
d = {1, 2, 3, 4, 5, 6, 7, 8, 9}
e = {i**3 for i in a if i > 5}
print(e)

# 字典进行列表推导式
stu = {'a': 1,
      'b': 2,
      'c': 3
      }

f = (key for key, value in stu.items())
print(f)
