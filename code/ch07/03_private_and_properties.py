# 03_private_and_properties.py - 私有屬性、封裝、與 @property 裝飾器的應用

# 1. 私有屬性與名稱修飾 (Name Mangling)
class BankAccountPrivate:
    def __init__(self, name, balance):
        self.name = name
        # 雙底線開頭屬性為私有屬性，防止外部直接讀寫
        self.__balance = balance

    # 提供公開方法 (Getter/Setter) 來安全操作私有屬性
    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("交易失敗：金額無效或餘額不足")

nick = BankAccountPrivate('Nick', 10000)
nick.deposit(5000)
print(f"安全取得餘額: {nick.get_balance()}")

try:
    # 外部嘗試直接存取私有變數會引發 AttributeError
    print(nick.__balance)
except AttributeError as e:
    print("補獲錯誤 (無法外部存取私有屬性):", e)

# 2. @property 裝飾器 (簡化 Getter/Setter)
class User:
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    # Getter: 將屬性偽裝成一般唯讀屬性
    @property
    def score(self):
        return self.__score

    # Setter: 當嘗試對屬性賦值時被呼叫，可在這做數值過濾與邏輯判斷
    @score.setter
    def score(self, new_score):
        if 0 <= new_score <= 100:
            self.__score = new_score
        else:
            print("錯誤：分數必須介於 0 與 100 之間！")

u = User("Albert", 85)
print("\n透過 @property 讀取分數:", u.score)
u.score = 95  # 觸發 setter
print("修改後的分數:", u.score)
u.score = -10 # 觸發 setter，且條件不符會被擋下
