#自定义支持关键字with的类。
#如果自定义类中实现了特殊方法__enter__()和__exit__()，
#那么该类的对象就可以像内置函数open()返回的文件对象一样支持with关键字来实现资源的自动管理。
class myOpen:
    def __init__(self, fileName, mode='r'):
        self.fp = open(fileName, mode)

    def __enter__(self):
        return self.fp

    def __exit__(self, exceptionType, exceptionVal, trace):
        self.fp.close()

with myOpen('test.txt') as fp:
    print(fp.read())
