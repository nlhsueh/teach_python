# 04_dunder_methods.py - 特殊方法 (Dunder Methods) 與運算子多載 (Operator Overloading)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __str__：當 print(obj) 或 str(obj) 時，回傳的易讀文字表達
    def __str__(self):
        return f"({self.x}, {self.y})"

    # __repr__：用於開發調試的正式字串表達
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    # 多載加法運算子 +
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    # 多載減法運算子 -
    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        return NotImplemented

    # 多載大於比較運算子 > (此處依據點到原點的距離平方進行比較)
    def __gt__(self, other):
        if isinstance(other, Point):
            dist1 = self.x**2 + self.y**2
            dist2 = other.x**2 + other.y**2
            return dist1 > dist2
        return NotImplemented

p1 = Point(3, 4)
p2 = Point(1, 2)

print("p1 的 str 印出:", p1)
print("p1 的 repr 表達:", repr(p1))

# 運算子多載測試
p3 = p1 + p2
p4 = p1 - p2
print("p1 + p2 = (3+1, 4+2) =", p3)
print("p1 - p2 = (3-1, 4-2) =", p4)

# 大於比較
print("p1 > p2 (點的距離比較):", p1 > p2)
