# 06_inheritance_override.py - 類別繼承 (Inheritance)、方法覆寫 (Override) 與 super() 呼叫

# 1. 父類別 (Base Class / Parent Class)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name} is walking.")

# 2. 子類別 Engineer (繼承 Person)
class Engineer(Person):
    def __init__(self, name, age, skill):
        # 呼叫父類別的建構子，初始化 name 和 age
        super().__init__(name, age)
        self.skill = skill

    # 覆寫 (Override) 父類別的 walk 方法
    def walk(self):
        print(f"Engineer {self.name} is walking fast because of a deployment deadline!")

    def fix(self):
        print(f"{self.name} is fixing bug with {self.skill}.")

# 3. 子類別 Manager (繼承 Person)
class Manager(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    # 覆寫 (Override) walk 方法
    def walk(self):
        print(f"Manager {self.name} is walking to a meeting room.")

    def plan(self):
        print(f"{self.name} is planning project for {self.department} department.")

# 實例化與多型 (Polymorphism) 測試
jack = Engineer('Jack', 30, 'Python')
mary = Manager('Mary', 40, 'Sales')
nick = Person('Nick', 25)

# 多型走訪：同樣是呼叫 walk()，不同類別展現不同的行為
group = [jack, mary, nick]
print("--- 多型走訪測試 ---")
for p in group:
    p.walk()

print("\n--- 子類別專屬方法 ---")
jack.fix()
mary.plan()
