# -*-coding:utf-8 -*-
'''
    类 = 特征 + 行为
'''


class Student(object):
    #name = ''
    #age = 0
    __count = 0

    #对象初始化函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #Student.count += 1
        #实例方法访问类变量
        #self.__class__.count += 1
        print('age: ', age, ' name: ', name)

    def print_profile(self):
        print('name: ', self.name)
        print('age: ', str(self.age))

    #类方法-类方法访问类变量
    @classmethod
    def countSum(cls):
        cls.__count += 1
        print(cls.__count)

    @staticmethod
    def add(x, y):
        return x+y

    @classmethod
    def getCount(cls):
        return cls.__count



stu = Student('Jack', 20)
stu.countSum()
#print(stu.count)
stu1 = Student('JackJones', 22)
stu1.countSum()

print('Student.count: ', Student.getCount())
print(Student.add(1, 2))
