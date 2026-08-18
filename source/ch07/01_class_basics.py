# 01_class_basics.py - 類別與物件宣告、建構子、屬性與方法

# 1. 基礎 People 類別
class People:
    # 建構子 (Constructor)
    def __init__(self, sex, age, name):
        self.sex = sex
        self.age = age
        self.name = name

p1 = People('male', 20, 'Nick')
print(f"p1 資料 -> 姓名: {p1.name}, 性別: {p1.sex}, 年齡: {p1.age}")

# 2. 貨幣轉換 Currency 類別
class Currency:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def to_twd(self):
        """將外幣轉換成台幣值"""
        if self.unit == 'USD':
            return self.value * 30
        elif self.unit == 'JPY':
            return self.value * 0.28
        return self.value

usd = Currency(100, 'USD')
jpy = Currency(1000, 'JPY')
print("100 USD 轉台幣:", usd.to_twd())
print("1000 JPY 轉台幣:", jpy.to_twd())

# 3. 基礎銀行帳戶 BankAccount
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance  # 目前先使用一般公開屬性

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("餘額不足！")

acc = BankAccount('Nick', 10000)
acc.deposit(5000)
acc.withdraw(3000)
print(f"{acc.name} 帳戶餘額: {acc.balance}")
