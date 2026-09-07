# 01_io_basic.py
# 知識點：程式的基本架構（輸入、處理、輸出）

# 1. 簡單的輸入與字串串接
name = input("What is your name: ") 
hello_to_you = "Hello " + name
print(hello_to_you)

# 2. 直接在 print 中進行運算
print("Nick's BMI is", 65 / (1.7 * 1.7))

# 3. 使用變數進行計算與輸出
name = "Nick"
weight = 65
height = 1.7
bmi = weight / (height * height)

# 結合字串與數值進行輸出
print(name + "'s BMI is", bmi)
