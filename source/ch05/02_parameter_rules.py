# 02_parameter_rules.py - 參數規則：關鍵字參數、預設參數、參數限制與型態提示

# 1. 關鍵字參數 (Keyword Arguments)
def hello1(name, msg):
    print("Hi, {}, {}".format(name, msg))

hello1('Nick', 'Good morning')
hello1(msg='Good morning', name='Nick')  # 指定關鍵字，順序可顛倒

# 2. 預設參數 (Default Parameters)
# 注意：在定義時，有預設值的參數必須排在沒有預設值的「必要參數」後面
def hello2(name, msg="Hello"):
    print("Hi, {}, {}".format(name, msg))

hello2('Nick')                 # 未傳遞第二個參數，使用預設值 "Hello"
hello2('Nick', 'Good morning') # 傳遞了第二個參數，覆蓋預設值

# 3. 位置專用與關鍵字專用參數 (Python 3.8+)
# `/` 之前的參數只能以位置傳遞，不可使用 key=value
# `*` 之後的參數只能以關鍵字傳遞，必須使用 key=value
def example(pos_only, /, standard, *, kw_only):
    print(f"pos_only: {pos_only}, standard: {standard}, kw_only: {kw_only}")

example("I am pos-only", "I am standard", kw_only="I am kw-only")
example("I am pos-only", standard="I am standard", kw_only="I am kw-only")

try:
    # 這會引發 TypeError，因為 pos_only 寫了關鍵字
    example(pos_only="error", standard="standard", kw_only="kw-only")
except TypeError as e:
    print("Type Error (pos-only 限制):", e)

try:
    # 這也會引發 TypeError，因為 kw_only 沒有以關鍵字指定
    example("pos-only", "standard", "kw-only")
except TypeError as e:
    print("Type Error (kw-only 限制):", e)

# 4. 現代型態提示 (Type Hints) with Union | (Python 3.10+)
def greet(name: str, age: int | None = None) -> str:
    if age is not None:
        return f"Hello {name}, you are {age} years old."
    return f"Hello {name}."

print(greet("Alice", 25))
print(greet("Bob"))
