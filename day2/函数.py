# _*_coding:utf-8 _*_
'''
Python函数多个返回值的使用方式
'''
def damage(skill1, skill3, skill2=10):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    damage3 = skill2 * 5 - 10
    damage4 = skill3 * 9 - 1
    return damage1, damage2, damage3, damage4


result1, result2, result3, result4 = damage(4)
print(result1, result2, result3, result4)
