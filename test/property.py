'''
property
将一个get方法转化为对象的属性，调用方法改为调用对象

setter
将一个set方法转换为对象的属性
@属性名.setter
'''

class Person:
    def __init__(self, name):
        self._name = name

    #利用property装饰器获取name的方法转化为属性
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

p1 = Person("wang")
p1.name = "xxx"
p1.get_name