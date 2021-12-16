# 开箱即用
# 为了实现开箱即用的思想，Python中为我们提供了一个模块的标准库
# 在这个标准库中，有很多很强大的模块我们可以直接使用
#   并且标准库会随Python的安装一同安装
# sys模块，它里面提供了一些变量和函数，使我们可以获取到Python解析器的信息
#   或者通过函数来操作Python解析器
# 引入sys模块
import sys 
# print(sys)

# pprint 模块它给我们提供了一个方法 pprint() 该方法可以用来对打印的数据做简单的格式化
import pprint

# sys.argv 
# 获取执行代码时，命令行中所包含的参数
# 该属性是一个列表，列表中保存了当前命令的所有参数
# print(sys.argv)

# sys.modules
# 获取当前程序中引入的所有模块
# modules是一个字典，字典的key是模块的名字，字典的value是模块对象
# pprint.pprint(sys.modules)

# sys.path
# 他是一个列表，列表中保存的是模块的搜索路径
# ['c:\\TestPython\\.vscode',
#  'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip',
#  'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python310\\DLLs',
#  'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python310\\lib',
#  'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python310',
#  'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages']
# pprint.pprint(sys.path)

# sys.platform 
# 表示当前Python运行的平台
# print(sys.platform)

# sys.exit()
# 函数用来退出程序
# sys.exit('程序出现异常，结束！')
# print('hello')

# os 模块让我们可以对操作系统进行访问
import os 

# os.environ
# 通过这个属性可以获取到系统的环境变量
# pprint.pprint(os.environ['path'])

# os.system()
# 可以用来执行操作系统的名字
# os.system('dir')
os.system('notepad')

c语言学习网站来了
1.C：https://github.com/TheAlgorithms/C
2.libhv：https://github.com/ithewei/libhv
3.CPlusPlusThings：https://github.com/Light-City/CPlusPlusThings
4.design-patterns-cpp：https://github.com/JakubVojvoda/design-patterns-cpp
5.tmux：https://github.com/tmux/tmux
6.netdata：https://github.com/netdata/netdata