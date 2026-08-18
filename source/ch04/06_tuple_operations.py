# 06_tuple_operations.py - Tuple 的宣告、不可變性、打包與開箱、結構化匹配

# 1. 建立與讀取
tup1 = ('Nick', 'FCU', 172, 75)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
tup4 = tuple([1, 2, 3, 4, 5])

# 唯讀測試 (以下操作會報錯，故用 try-except 封裝展示)
try:
    tup2[0] = 100
except TypeError as e:
    print('Tuple 修改錯誤:', e)

t = ('a', 'b', 'c', 'd', 'e', 'f')
print('第 0 個元素:', t[0])
print('切片 t[1:4]:', t[1:4])
print('倒數第 1 個:', t[-1])

# 2. 元組打包與開箱 (Unpacking)
person = ('male', 10, 'nick')  # 打包 (pack)
sex, age, name = person        # 開箱 (unpack)
print(f'開箱結果: 性別={sex}, 年齡={age}, 姓名={name}')

# 3. 現代結構化模式匹配 match-case (Python 3.10+)
def run_cmd(cmd):
    match cmd:
        case ["move", direction]:
            print(f"指令匹配成功 -> 移動到方向: {direction}")
        case ["jump", x, y]:
            print(f"指令匹配成功 -> 跳躍至座標: ({x}, {y})")
        case ["attack", *targets]:
            print(f"指令匹配成功 -> 攻擊多個目標: {targets}")
        case _:
            print("指令匹配失敗 -> 無法識別！")

run_cmd(["move", "North"])
run_cmd(["jump", 15, 35])
run_cmd(["attack", "goblin1", "goblin2", "boss"])
