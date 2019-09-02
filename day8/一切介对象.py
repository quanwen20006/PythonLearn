'''
    1：函数和类可以赋值给变量
    2：添加到集合中
    3：可以作为传递参数
    4：可以当做函数的返回值
'''
def ask(name='jack'):
    print('jack')


class Person(object):
    def __init__(self):
        print('person')

# 函数当返回值
def decoratror_func():
    print('dec start...')
    return ask

obj_list = []
obj_list.append(ask)
obj_list.append(Person)

for item in obj_list:
    item()

my_func = ask
my_func('jones')
my_func1 = Person
my_func1()

my_func2 = decoratror_func()
my_func2('Tom')

a="123"
print('实例所属类：', type(a))
print('实例所属类由 %s ：创建 '% type(str))
print('实例所属类：',type(type))
print(my_func1.__bases__)
print(object.__bases__)
print('type由%s ：',type.__bases__)