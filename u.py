class people:
    def __init__(me, name, height, age):
        me.name = name
        me.height = height
        me.age = age


a = people("abc", 166, 27)
print(a.name)
print(a.age)


class person():
    '''人类包含姓名年龄身高等属性和跑方法'''
    def __init__(self, name, height, age):
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        print("Run")

b = person("xiaomingwang", 1.67,27)
print(b.name)
print(b.age)
print(b.height)
print(b)