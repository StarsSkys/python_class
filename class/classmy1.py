#下面的代码创建了一个餐馆类，并且创建了一个餐馆实例（对象）
#每个类对应一个类对象，用以存储类的基本信息
class Restaurant():            #类对象
    """一个表示餐馆的类"""      #类描述
    restaurant_star = 3   #类属性，直接在类中定义用类名点属性名访问
    count = 0

    def __init__(self, name, cuisine_type):  #类的构造函数，类实例化时使用的函数
        """初始化餐馆"""
        self.name = name.title()         #实例属性，在类中self.属性名
        self.cuisine_type = cuisine_type
        Restaurant.count += 1

    def describe_restaurant(self):   #类的方法
        """显示餐馆信息摘要"""
        msg = self.name + "服务很好"+\
self.cuisine_type + "."
        print ("\n" + msg)

    def open_restaurant (self):
        """显示一条消息，指出餐馆正在营业"""
        msg = self.name + "餐馆正在营业,欢迎光临!"
        print ("\n" + msg)

restaurant = Restaurant("星空披萨", 'pizza') #实例化即创建一个对象

print(restaurant.name)       #实例属性，在类 外对象名点属性名  #类中直接包含的语句会被执行
print(restaurant.cuisine_type)   #一般不这样使用
print(Restaurant.restaurant_star)

restaurant.describe_restaurant()  #对象名点方法名/属性名调用方法 
restaurant.open_restaurant()      #实例方法，对象名点方法名（参数）

 


