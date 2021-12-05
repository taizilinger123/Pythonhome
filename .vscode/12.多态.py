# 多态是面向对象的三大特征之一
# 多态从字面上理解是多种形态
# 狗（狼狗，藏獒，哈士奇，古牧。。。）
# 一个对象可以以不同的形态去呈现
class A:
    def __init__(self,name):
        self._name = name  

    @property
    def  name(self):
        return  self._name 
    
    @name.setter
    def  name(self,name):
        self._name = name 

class B:
    def __init__(self,name):
        self._name = name  

    @property
    def  name(self):
        return  self._name 
    
    @name.setter
    def  name(self,name):
        self._name = name 
class C:
    pass

a = A('孙悟空')
b = B('猪八戒')
c = C()
# 定义一个函数  
# 对于say_hello()这个函数来说，只要对象中含有name属性，它就可以作为参数传递
# 这个函数并不会考虑对象的类型，只要有name属性即可
def  say_hello(obj):
    print('你好 %s'%obj.name)

say_hello(b)