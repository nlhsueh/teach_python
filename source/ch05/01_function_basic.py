# 01_function_basic.py - 函式基本定義、回傳值與 Docstring 說明

# 1. 最簡單的函式與參數
def hello2(p): 
    print('Hello', p)
    
hello2("Java")    # 呼叫函式，帶入參數
hello2("Python")

# 2. 多重條件判斷與回傳 (Return)
def find_max(a, b, c):
    """
    找出三個參數中的最大值並回傳。
    此三引數必須是可以進行大小比較的型態。
    """
    if a > b:
        if a > c:
            m = a
        else:
            m = c
    elif b > c:
        m = b
    else:
        m = c
    return m    

print("最大值:", find_max(1, 2, 3))
print("最大值:", find_max(3, 2, 1))
help(find_max)  # 印出函式的說明文件 (Docstring)

# 3. 實用案例: 計算 BMI
def get_bmi(tall, weight):
    """ 
    基於傳入的身高與體重計算人體的 BMI 並回傳。
    身高 tall 必須以公尺為單位，體重 weight 以公斤為單位。
    """
    bmi_value = weight / (tall * tall)
    return round(bmi_value, 2)

bmi = get_bmi(1.72, 80)
print("計算出的 BMI 為:", bmi)
