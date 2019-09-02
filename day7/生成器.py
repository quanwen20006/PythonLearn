'''
    生成器
'''


def gen(max):
    n = 0
    while n <= max:
        n += 1
        # yield 会把执行的结果返回，但是不退出，下次再调用，被yield修饰的值，加1
        yield n

g = gen(100)
#for i in g:
#    print(i)

print(next(g))
print(next(g))
print(next(g))
