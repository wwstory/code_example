from build.demo import *

# ani1 = Animal() # 1 不应该允许构建纯虚函数
dog1 = Dog()
print(dog1.go(3))
print(call_go(dog1))

class Cat(Animal):  # 添加PyAnimal提供python继承扩展抽象类
    def go(self, n_times):
        return "meow! " * n_times

c = Cat()
print(call_go(c))

class DogX(Dog):
    def go(self, n_times):
        return "wow X!" * n_times
dogx = DogX()
print(dogx.go(3))
