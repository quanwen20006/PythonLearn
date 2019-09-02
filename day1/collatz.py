#-*- coding:utf-8 -*-

'''
Collatz序列,根据用户输入的值，查找得到1
'''
def collatz(number):
    result = 0
    if number % 2 == 0:
        result = int(number/2)
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result


if __name__ == '__main__':
    while True:
        try:
            temp = int(input('请输入： '))
            if temp == 1:
                collatz(temp)
                break
            else:
                collatz(temp)
        except ValueError:
            print('请输入数字')
