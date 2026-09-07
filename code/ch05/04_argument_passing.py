# 04_argument_passing.py - 引數傳遞機制：不可變與可變物件、複製後傳 (Copy and pass)

# 1. 傳遞不可變物件 (Immutable, 如 int, str, tuple)
def plus1(aNumber):
    # aNumber 只是局部變數，修改它不會影響外部傳入的變數
    aNumber += 1
    print("Inside plus1:", aNumber)

# 2. 傳遞可變物件 (Mutable, 如 list, dict, set)
def plus2(aList):
    # aList 指向同一個列表物件，就地修改會影響外部變數
    for i in range(len(aList)):
        aList[i] += 1
    print("Inside plus2:", aList)

a, m = 1, [1, 2]
print('-- Before Calling function --')
print("a (int) =", a, ", m (list) =", m)

print('-- After Calling function --')
plus1(a)
plus2(m)
print("a (int) =", a, ", m (list) =", m)

# 3. 複製後傳 (Copy and pass)
# 如果不想讓函式修改原本的可變物件，呼叫前應建立副本並傳遞
print('-- Using copy and pass --')
m2 = [1, 2]
plus2(m2.copy())
print("Original m2 (應保持不變 [1, 2]):", m2)
