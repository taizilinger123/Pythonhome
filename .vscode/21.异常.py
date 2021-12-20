# print('hello')
# try:
#     # try中放置的是有可能出现错误的代码
#     print(10/0)
# except:
#     # except中放置的是出错以后的处理方式
#     print('哈哈哈，出错了~~~')
# else:
#     print('程序正常执行没有错误')
# print('你好')

# print(10/0)
print(NameError)

def fn():
    print('Hello fn')
    print(a) 
    print(10/0)

def fn2():
    print('Hello fn2')
    fn()

def fn3():
    print('Hello fn3')
    fn2()

fn3()

# Traceback (most recent call last):
#   File "c:\TestPython\.vscode\21.异常.py", line 25, in <module>
#     fn3()
#   File "c:\TestPython\.vscode\21.异常.py", line 23, in fn3
#     fn2()
#   File "c:\TestPython\.vscode\21.异常.py", line 19, in fn2
#     fn()
#   File "c:\TestPython\.vscode\21.异常.py", line 15, in fn     #数字从小到大看最小的数字剩下的都是因为调用它才出错的，这里出现的问题
#     print(10/0)
# ZeroDivisionError: division by zero
