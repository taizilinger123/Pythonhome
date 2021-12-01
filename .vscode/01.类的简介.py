a = int(10)
b = str('hello')

#print(a, type(a))
#print(b, type(b))

class MyClass():
    pass  
# print(MyClass)
nc = MyClass()
nc_1 = MyClass()
#print(nc,type(nc))

result = isinstance(nc, MyClass)
#print('result=', result)

print(id(MyClass), type(MyClass))

