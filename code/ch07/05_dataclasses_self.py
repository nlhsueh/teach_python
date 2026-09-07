# 05_dataclasses_self.py - 現代 OOP 優化：@dataclass 與 Self 型態提示

from dataclasses import dataclass
from typing import Self

# 1. 使用 @dataclass (Python 3.7+)
# 自動生成 __init__、__repr__、__eq__ 比較等樣板程式碼
@dataclass
class Student:
    name: str
    student_id: str
    grades: list[int]

s1 = Student('Nick', 'S9201201', [90, 72, 100])
s2 = Student('Nick', 'S9201201', [90, 72, 100])

# 印出結果 (自動產生的友善 repr 文字)
print("s1 物件內容:")
print(s1)

# 比較物件 (自動生成的 eq 內容相等比較，而非記憶體位置)
print("s1 與 s2 內容是否相同:", s1 == s2) # True

# 2. 方法傳回本身的 Self 型態提示 (Python 3.11+)
class Book:
    def __init__(self, title: str):
        self.title = title

    # rename 方法會回傳實例本身，標註為 Self 代表傳回 Book 本身類型
    def rename(self, new_title: str) -> Self:
        self.title = new_title
        return self  # 回傳物件本身，方便進行鏈式呼叫 (Chaining)

b = Book("Python 101")
# 鏈式呼叫範例
b.rename("Modern Python").rename("Advanced Python (3.10+)")
print("最終書名:", b.title)
