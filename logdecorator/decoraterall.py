import  functools
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logging.basicConfig(level=logging.NOTSET) 
# # 将信息打印到控制台上
# logging.info('this is a loggging info message')
# logging.debug('this is a loggging debug message')
# logging.warning('this is loggging a warning message')
# logging.error('this is an loggging error message')
# logging.critical('this is a loggging critical message')

def log(func):
    @functools.wraps(func)                           #这一句的功能是使被装饰器装饰的函数的函数名不被改变，
    def wrapper(*args, **kwargs):
        logging.debug("开始打日志，程序开始。。。。。")
        logging.debug('原来函数的方法名:{}'.format(func.__name__))    #这里使用了装饰器的参数k
        r = func(*args, **kwargs)
        logging.debug("程序结束。。。。。")
        return r
    return wrapper


def log1(func):
    logging.warn("这是log1外层，不在返回函数里面的")
    @functools.wraps(func)
    def outer(*a,**b):
        logging.warn("这是log1 里面的内容")
        r = func(*a,**b)
        logging.warn("执行完log1")
        return r
    return outer

def log2(*dddargs):
    def wapper(func):
        logging.warn("这是log2外层，不在返回函数里面的")
        @functools.wraps(func)
        def dalao(*args):
            logging.warn("这是log2 里面的内容")
            print(f"这是原来函数的参数{args}")
            print(f"这是第一个参数{dddargs[0]}")
            print(f"这是第er个参数{dddargs[1]}")
            r = func(*dddargs)
            logging.warn("执行完log2")
            return r
        return dalao
    return wapper


# 类修饰器
import types

def deco(cls):
    for key, method in cls.__dict__.items():
        if isinstance(method, types.FunctionType):
            print(key, ':', method.__name__)
    return cls

@deco
class Test:
    a = 1
    b = 2
    def __init__(self):
        pass

    def foo(self):
        pass

Test().foo()