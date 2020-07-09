from decoraterall  import log,log2,log1
import logging

@log
def test1():
    print("zheshi 程序里 面的东西。。。")



@log1
@log2(333,444)
def test2(*args):
    print("在函数中执行",args[0])
    logging.debug("在函数中使用logging111111111111111111111")
    print("在函数中执行",args[1])



test2(111,123,12,31,23)
# test1()