#类的继承的几个示例

class User():                   #父类
    """一个表示用户的简单类。"""
 
    def __init__(self, first_name, last_name, username, email, location):
        """初始化用户。"""
        self.first_name = first_name #构造用户的基本信息
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0
 
    def describe_user(self):
        """显示用户信息摘要。"""
        print("\n" + self.first_name + " " + self.last_name)
        print("  用户姓名: " + self.username)
        print("  用户电子邮件： " + self.email)
        print("  用户地点: " + self.location)
 
    def greet_user(self):
        """向用户发出个性化问候。"""
        print("\n欢迎回来, " + self.username + "!")
 
    def increment_login_attempts(self):   #尝试登录次数逐渐增多
        """将属性login_attempts的值加1。"""
        self.login_attempts += 1
 
    def reset_login_attempts(self):
        """将login_attempts重置为0。"""
        self.login_attempts = 0



class Admin(User):             #子类
    """有管理权限的用户。"""
 
    def __init__(self, first_name, last_name, username, email, location):
        """初始化管理员。"""
        super().__init__(first_name, last_name, username, email, location) #继承父类的属性
 
        # 将权限集初始化为空。
        #这行代码让Python创建一个新的Privileges并将该实例存储在属性self.privileges
        #每当方法__init__()被调用时，都将执行该操作；因此现在每个Admin的实例都包含一个自动创建的Privileges实例。
        self.privileges = Privileges()  #将Privileges类用作class类的属性
 
class Privileges():
    """一个存储管理员权限的类。"""
 
    def __init__(self, privileges=[]):
        self.privileges = privileges
 
    def show_privileges(self):     #显示管理员的权限
        print("\n管理员特权:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("用户并没有这项特权.")
 
eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska') #创建管理员对象
eric.describe_user()     #子类调用父类的方法
 
eric.privileges.show_privileges()   #类调用被用作属性的类的方法#展示一般用户权限
 
print("\n管理员增加的特权...")
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()   #展示管理员的特权




#继承list类型的新类型重载其中的加法运算
class NewList(list):
    def __add__(self, other):
        result = []
        for i in range (len(self)):
            try:
                result.append(self[i]+ other[i])
            except:
                result.append(self[i])
        return result
ls = NewList([1,2,3,4,5,6])
lt = NewList([1,2,3,4])
print(ls + lt)
#输出[2, 4, 6, 8, 5, 6]，的应位置元素相加

