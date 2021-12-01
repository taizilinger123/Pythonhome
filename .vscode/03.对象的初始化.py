class Person:
    def __init__(self,name):
        self.name = name
    def say_hello(self):
        print('大家好，我是%s'%self.name)

p1 = Person('孙悟空')
p2 = Person('猪八戒')
p3 = Person('唐三藏')
p4 = Person('沙和尚')

p1.say_hello()
p2.say_hello()
p3.say_hello()
p4.say_hello()