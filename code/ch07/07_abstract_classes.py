# 07_abstract_classes.py - 抽象類別 (Abstract Classes) 與抽象方法 (Abstract Methods)

from abc import ABCMeta, abstractmethod

# 1. 定義抽象類別 (Abstract Class)
# 使用 metaclass=ABCMeta 宣告，無法被直接實例化，主要作為規範子類別的界面
class GuessGame(metaclass=ABCMeta):
    
    # 抽象方法：所有繼承的子類別「必須」實現此方法，否則會報錯
    @abstractmethod
    def message(self):
        pass

    @abstractmethod
    def guess(self):
        pass

    # 具體方法：子類別可以直接繼承或覆寫
    def go(self):
        print("遊戲啟動...")
        self.message()
        self.guess()

# 2. 實作一個具體的遊戲子類別 (Concrete Class)
class NumberGuessGame(GuessGame):
    def __init__(self, target):
        self.target = target

    # 實現抽象方法 message
    def message(self):
        print("歡迎來到猜數字遊戲！")

    # 實現抽象方法 guess
    def guess(self):
        # 這裡僅進行靜態的模擬展示
        simulated_guess = 50
        print(f"模擬輸入猜測: {simulated_guess}")
        if simulated_guess == self.target:
            print("答對了！")
        else:
            print(f"答錯了，答案是 {self.target}")

# 3. 測試執行
# 嘗試實例化抽象類別會引發 TypeError
try:
    g = GuessGame()
except TypeError as e:
    print("無法實例化抽象類別提示:", e)

# 正常使用具體實作的子類別
game = NumberGuessGame(target=50)
game.go()
