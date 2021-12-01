class Dog:
    '''
    表示狗类
    '''
    def __init__(self,name,age,gender,height):
        self.name = name 
        self.age = age 
        self.gender = gender
        self.height = height 

    def  jiao(self):
        '''
        狗叫的方法 
        '''
        print('汪汪汪~~~')
    def  yao(self):
        '''
        狗咬的方法 
        '''
        print('我咬你~~~')
    def  run(self):
        print('%s快乐的奔跑着~~'%self.name)
    
    
d = Dog('旺财',8,'male',30)
d.age= -10
print(d.age)

# print(d.name, d.age, d.gender, d.height)