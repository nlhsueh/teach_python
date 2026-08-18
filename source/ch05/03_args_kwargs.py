# 03_args_kwargs.py - 不定個數參數 *args 與 **kwargs

# 1. 變動位置參數 (*args) - 以 Tuple 收集
def avg(name, *grade): 
    # grade 在函式內部是一個 tuple
    print("Type of grade: {}, values are: {}".format(type(grade), grade))
    if len(grade) == 0:
        return 0
    total = sum(grade)
    return total / len(grade)

print("Nick 的平均分數:", avg("Nick", 90, 80, 70, 100))
print("John 的平均分數:", avg("John"))

# 2. 變動關鍵字參數 (**kwargs) - 以 Dict 收集
def intro(name, **kwargs):
    # kwargs 在函式內部是一個 dict
    print("Type of kwargs: {}, values are: {}".format(type(kwargs), kwargs))
    print(f"Name: {name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

intro("Albert", age=20, city="Taichung", major="Information")
