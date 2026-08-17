
Ch02 程式結構
===

## 2.1 程式的基本架構：輸入、處理、輸出

我們先來看一個典型的程式處理架構，包含輸入、處理、輸出：

```python
name = input("What is your name: ") 
helloToYou = "Hello " + name
print (helloToYou)

## using variable in statement
print ("Nick's BMI is", 65/(1.7*1.7))

name = "Nick"
weight = 65
height = 1.7
BMI = weight / (height*height)

print (name + "'s BMI is", BMI)
```

這段程式碼是一個簡單的Python程式，用於處理用戶的輸入，執行一些計算，然後輸出結果。讓我們逐行解釋這個程式碼：

1. `name = input("What is your name: ")`: 這一行請求用戶輸入其名字，並將輸入的字符串存儲在名為 `name` 的變數中。其中 `What is your name: `是在互動過程中的提示字。
2. `helloToYou = "Hello " + name`: 這一行創建一個新的字串變數 `helloToYou`，它包含了一個問候詞 "Hello " 和用戶輸入的名字。
3. `print(helloToYou)`: 這一行輸出了 `helloToYou`的值，結果顯示在控制台。假設我們剛剛輸入的 name 是 `John`, 則此時會輸出：`Hello John`。此時的 `+`的作用是做字串相連。
4. `print("Nick's BMI is", 65 / (1.7 * 1.7))`: 這一行計算並輸出了一個假想人物 Nick 的BMI（身體質量指數），BMI的計算公式是體重（kg）除以身高（米）的平方。計算結果顯示在控制台。此時的 `+`左邊是字串，右邊是數字， Python 會自動將數字轉換為字串型態，再進行字串相連。
5. 接下來的幾行程式碼利用變數來儲存身高和體重，並且使用這些變數來計算BMI。計算結果顯示在控制台。

## 2.2 變數
### 2.2.1 什麼是變數

* 用來儲存特定的值，以作為後續的應用
* 雖然在 Python 中不須特別指名型態，但每個變數是有形態的
* 注意變數的型態、命名規則、命名慣例


```python
## 變數的命名與宣告
x = 100
y = 200
r = 100 s = 200 # 這是錯的
z = 100; w=200  # 利用 ; 來區分敘述句				
p = q = 100
name, eng, math, phy = "Nick", 92, 88, 32	
```
第七行的效果相當於 `name="Nick"; eng=92; math=88;phy=32`。

### 2.2.2 命名規則

主要由英文，數字，_ 所構成
例如 employee_code, employee_code2, employeeCode 等


* 不可數字開始: 3employee 錯誤
* 不可使用特殊字元
* &, #, * @ 等特殊字元皆不可
* 大小寫不同
* employee, Employee 代表的是不同的變數
* 不可與 保留字 相同
* 例如 for, else, import 等都是系統的保留字

以下變數命名都錯誤：

```python
and = 1     # Error, and 是保留字
@employ = 1 # Error, 不可包含 @ 特殊字
```


有意義的命名很重要：

```python
grade = 100
temperature = 8.9
name = "John"
teacherName = 'Nick'
isTeacher = True
getPass = False
```

保留字

以下是 Python  保留字，不可以當成變數名稱

```
False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise
```

### **2.2.3 隨堂測驗**

**第一題**

下列哪一個變數名稱在 Python 中是**無效的 (Invalid)**？

A) `_my_var`
B) `my-var`
C) `myVar2`
D) `MYVAR`

---

**第二題**

在 Python 中，`total` 和 `Total` 這兩個變數名稱，請問它們代表的意義是？

A) 完全相同，因為 Python 不區分大小寫。
B) 語法錯誤，變數名稱不能使用大寫字母。
C) 代表兩個不同的變數，因為 Python 區分大小寫。
D) 只有 `total` 是有效的變數名稱。

---

**第三題**

下列哪一個選項**不能**被用來當作變數名稱？

A) `age`
B) `import`
C) `address`
D) `pi`

---

<details>
<summary>點擊查看【隨堂測驗】答案與解析</summary>

**答案與回饋**

* **第一題：B) `my-var`**
    * **回饋**：Python 的變數名稱只能包含**英文字母 (a-z, A-Z)**、**數字 (0-9)** 和**底線 (_)**。連字號 (`-`) 是無效的字元，它會被直譯器視為減法運算子。

* **第二題：C) 代表兩個不同的變數，因為 Python 區分大小寫。**
    * **回饋**：Python 是一種**區分大小寫 (case-sensitive)** 的語言。因此，`total`、`Total`、`TOTAL` 都會被視為三個獨立且不同的變數。

* **第三題：B) `import`**
    * **回饋**：`import` 是 Python 的**保留字 (Reserved Keyword)** 或稱為關鍵字。這些字在語言中有特殊的語法功能（例如 `import` 用於匯入模組），因此不能被用作任何識別符（如變數名、函式名）的名稱。

</details>

### 2.2.4 變數型態

變數型態是程式語言中用來**分類資料**的標籤。你可以把它想像成一個貼在儲存資料的盒子（變數）上的標籤，這個標籤明確地告訴電腦這個盒子裡裝的是什麼種類的東西。


**為什麼需要變數型態？**

簡單來說，變數型態決定了電腦**如何理解**一份資料，以及**可以對它做什麼操作**。如果沒有型態，電腦將無法區分數字和文字，也無法進行有意義的運算。

主要有以下三個原因：

1.  **決定合法的操作**
    這是最核心的原因。資料的型態決定了它能參與的運算。
    * **數字**可以進行數學運算（加、減、乘、除）。
        ```python
        price = 80
        quantity = 2
        total_cost = price * quantity  # 合法操作，結果為 160
        ```
    * **文字**可以進行串接、分割等操作，但不能拿來相乘。
        ```python
        greeting = "Hello"
        target = "World"
        message = greeting + ", " + target  # 合法操作，結果為 "Hello, World"
        # error_operation = greeting * quantity # 這會產生非預期的結果或錯誤
        ```
    如果沒有型態區分，電腦就不知道 `+` 到底是要做數字相加，還是文字串接，從而導致混亂與錯誤。

2.  **有效管理記憶體**
    電腦需要為儲存的資料分配記憶體空間。不同的資料型態佔用的空間大小不同。
    * 儲存一個整數 (`123`) 所需的空間，遠小於儲存一本小說（一長串文字）。
    * 明確的型態讓電腦能精準地分配恰到好處的記憶體，從而更有效率地利用系統資源。

3.  **提高程式的可讀性與正確性**
    變數型態讓程式碼的意圖更加清晰。當你看到一個變數 `age` 被賦予為整數型態時，你立刻就能理解它的用途。如果有人不小心把它寫成文字，後續的程式在進行年齡計算時就會出錯，而型態系統能幫助我們在早期就發現這類型的錯誤。

**Python 中常見的基本變數型態**

Python 會根據你賦予的值**自動推斷**變數的型態，但背後的型態概念依然存在。

* **整數 (Integer, `int`)**
    就是不帶小數點的數字，用來計數或表示完整的個體。
    ```python
    student_count = 40
    score = -5
    ```

* **浮點數 (Floating-point, `float`)**
    就是帶有小數點的數字，用於需要更高精確度的計算。
    ```python
    pi = 3.14159
    temperature = 26.5
    ```

* **字串 (String, `str`)**
    用來表示任何文字資料，必須用單引號 (`'`) 或雙引號 (`"`) 包起來。
    ```python
    school_name = "逢甲大學"
    motto = 'Life is short, use Python.'
    ```

* **布林值 (Boolean, `bool`)**
    只有兩種可能：**`True`** (真) 或 **`False`** (假)，主要用於邏輯判斷。
    ```python
    is_registered = True
    has_error = False
    ```

你可以隨時使用 `type()` 函式來檢查一個變數的型態：
```python
age = 25
print(type(age))  # 輸出: <class 'int'>

name = "Alice"
print(type(name)) # 輸出: <class 'str'>
```
Python 中常見的變數型態：

| 變數型態       | 描述                                                          | 範例                 |
|----------------|--------------------------------------------------------------|----------------------|
| 整數（int）    | 用於表示整數值                                               | `5`, `-10`, `1000`  |
| 浮點數（float）| 用於表示帶有小數部分的數值                                   | `3.14`, `-0.5`, `2.0`|
| 字串（string） | 用於表示文本或字符序列                                       | `'Hello'`, `"Python"`|
| 布林值（bool） | 用於表示True（真）或False（假）的布林值                       | `True`, `False`      |
| 列表（list）    | 用於表示有序的可變序列，可以包含多種數據類型               | `[1, 2, 3]`, `['apple', 'banana', 'cherry']` |
| 元組（tuple）   | 用於表示有序的不可變序列，和列表類似，但元素不可更改       | `(1, 2, 3)`, `('red', 'green', 'blue')` |
| 集合（set）     | 用於表示無序的不可重複元素集合                               | `{1, 2, 3}`, `{'apple', 'banana', 'cherry'}` |
| 字典（dict）    | 用於表示鍵-值對的集合，每個鍵都與一個值相關聯             | `{'name': 'John', 'age': 30}` |
| 範圍（range）   | 用於表示一個整數範圍，通常在迴圈中使用                       | `range(0, 5)`        |
| NoneType（None）| 用於表示空值或缺少值的特殊型態                             | `None`               |

以上表格提供了每種變數型態的描述和示例，以幫助你理解它們的不同用途。

```python
a = 100       # int 型態
b = 8.9       # float 型態
c = "John"    # str 字串型態
d = 'Nick'    # str 字串型態
e = True      # 布林 boolean 型態
f = False     # 布林 boolean 型態

# why 變數的型態?
a = 1
b = 2
print (a+b)   # 印出 3

a = '1'
b = '2'
print (a+b)   # 印出 12
# print (a/b)   # TypeError: unsupported operand type(s) for /: 'str' and 'str' (字串無法進行除法)

x = 'apple'
y = 'banana'
print (x+y)   # 印出 applebanana

# print (x/y)   # Error (字串無法進行除法)
```

#### 檢查型態

透過 `type()` 來檢查型態：

```python
grade = 89
temperature = 32.5
name = 'Nick'
isTeacher = True

type(grade)         # int
type(temperature)   # float
type(name)          # str
type(isTeacher)     # bool
type(None)          # NoneType

# check if a given type
type (grade) == int      # True 

isinstance(grade, float) # False
isinstance('two', str)   # True
isinstance(2==2, bool)   # True
```

`isinstance` 若直翻為中文是 `是實體` 的意思，因為 `float` 等型態都是一種類別，而數值 `2`, `"two"` 等是一個實體，`isinstance`就是用來檢驗一個實體是否歸屬於該類別的方法。這個在後面的章節（物件導向設計）會有更詳細的解說。


#### 型態轉換

```python
# 將一個物件轉換為指定的型態
float(2)   # 將整數 2 轉換為浮點數 2.0
int(2.9)   # 將浮點數 2.9 轉換為整數 2 (無條件捨去小數)
str(2.9)   # 將浮點數 2.9 轉換為字串 '2.9'

# 數值零、None、以及空的容器(container)會被轉換為 False
bool(0)     # 數字 0        => False
bool(None)  # None 物件     => False
bool('')    # 空字串        => False
bool([])    # 空串列 (list) => False
bool({})    # 空字典 (dict) => False

# 非空的容器以及非零的數值會被轉換為 True
bool(2)       # 非零數字     => True
bool('two')   # 非空字串     => True
bool([2])     # 非空串列     => True
```

### 進階：電腦的秘密語言：深入理解 ASCII

我們在程式中理所當然地使用 `'A'`, `'B'`, `'!'` 等字元，但你有沒有想過，電腦內部是如何儲存這些符號的？

**核心觀念：電腦只懂數字**

電腦的本質是一個只會處理數字的機器，更精確地說，它只懂 0 和 1。它不認識英文字母、不懂中文，也不知道什麼是標點符號。因此，為了讓電腦能夠處理和儲存文字，工程師們必須建立一套「**翻譯規則**」。

這套規則就像一本**密碼本**，它為每一個人類看得懂的字元，都指定一個獨一無二的數字編號。當我們按下鍵盤上的 'A' 時，電腦實際上儲存的是它對應的數字編號。

**ASCII：最早的通用密碼本**

**ASCII** (American Standard Code for Information Interchange，美國資訊交換標準碼) 就是歷史上最重要、最普及的一本「密碼本」。

* 它定義了 128 個最常用的字元所對應的數字編號（從 0 到 127）。
* 這些字元包含了：
    * 英文大寫字母 (`A` 到 `Z`)
    * 英文小寫字母 (`a` 到 `z`)
    * 數字 (`0` 到 `9`)
    * 常用的標點符號 (如 `!`, `?`, ` ` (空格) 等)
    * 一些控制字元 (如換行、Tab 等)

例如，根據 ASCII 這本密碼本的規定：
* 當電腦看到數字 **65**，它就知道要顯示字元 **'A'**。
* 當電腦看到數字 **97**，它就知道要顯示字元 **'a'**。
* 當電腦看到數字 **49**，它就知道要顯示字元 **'1'**。

這個統一的標準，確保了早期不同電腦之間可以正確地交換與顯示文字資訊。

**從 ASCII 到 Unicode：一本更完整的全球密碼本**

ASCII 的缺點很明顯：它只收錄了英文世界的字元。那像「嗨」、「€」、「😂」這些符號怎麼辦呢？

為了解決這個問題，一個更全面的標準 **Unicode** 應運而生。Unicode 的目標是為**全世界所有語言的每一個字元**都提供一個唯一的數字編號。它是一本超級全球密碼本，收錄了數十萬個字元。

**重點**：**Unicode 完全相容 ASCII**。Unicode 的前 128 個編號，與 ASCII 的定義一模一樣。因此，在現代程式設計中（包括 Python），我們通常談論的是 Unicode，但當我們處理英文字元時，其背後的編碼值與傳統的 ASCII 是完全相同的。

**Python 中的字元與數字轉換**

Python 提供了兩個簡單的內建函式，讓我們可以在這本「全球密碼本」中自由查詢。

| 函式 | 描述 | 範例 |
| :--- | :--- | :--- |
| `ord()` | **查詢字元的數字編號** (Order) | `ord('A')` 返回 `65`，因為 'A' 的編碼是 65。 |
| `chr()` | **用數字編號反查字元** (Character) | `chr(65)` 返回 `'A'`，因為 65 號對應的字元是 'A'。 |

```python
# 使用 ord() 查詢字元的編碼
print(f"字元 'A' 的 Unicode 編碼是: {ord('A')}")  # 輸出：65
print(f"字元 'a' 的 Unicode 編碼是: {ord('a')}")  # 輸出：97
print(f"字元 '1' 的 Unicode 編碼是: {ord('1')}")  # 輸出：49
print(f"字元 '嗨' 的 Unicode 編碼是: {ord('嗨')}") # 輸出：21995

# 使用 chr() 用編碼反查字元
print(f"編碼 66 對應的字元是: {chr(66)}")      # 輸出: B (因為 65 是 'A', 66 就是 'B')
print(f"編碼 21996 對應的字元是: {chr(21996)}")  # 輸出: 嗨
```

**實際應用：為什麼要進行轉換？**

了解字元與數字的轉換，可以讓我們進行一些單純處理字串時無法做到的運算。例如，**取得下一個英文字母**：

```python
# 目標：給定一個大寫字母，找出它的下一個字母
current_char = 'C'

# 1. 先將字元轉為數字
current_code = ord(current_char)  # ord('C') -> 67

# 2. 對數字進行數學運算
next_code = current_code + 1      # 67 + 1 -> 68

# 3. 再將新的數字轉回字元
next_char = chr(next_code)        # chr(68) -> 'D'

print(f"'{current_char}' 的下一個字母是 '{next_char}'")
# 輸出: 'C' 的下一個字母是 'D'
```


> [!NOTE]
> :football: 寫一個程式，利用 ord() 及 chr() 和迴圈印出 a-z 26 個字母。
>
> 輸出如下：
> > The ASCII code of a is  97
> > a b c d e f g h i j k l m n o p q r s t u v w x y z

<details>
<summary>點擊查看參考解答與說明</summary>

```python
a_code = ord('a')
print ('The ASCII code of a is ', str(a_code))
for i in range(a_code, a_code+26):
  print (chr(i), end=' ')
```
這段程式碼的目的是列印小寫英文字母 `'a'` 到 `'z'` 的ASCII編碼以及它們的字符表示形式。讓我們逐行解釋這個程式碼：

1. `a_code = ord('a')`：這一行計算小寫字母 `'a'` 的ASCII編碼，並將其儲存在名為 `a_code` 的變數中。在ASCII編碼中，小寫 `'a'` 的編碼是97。
2. `print('The ASCII code of a is ', str(a_code))`：這一行輸出一條消息，顯示 `'a'` 的ASCII編碼。它使用 `str(a_code)` 將整數 `a_code` 轉換為字符串以進行輸出。
3. `for i in range(a_code, a_code+26):`：這是一個for迴圈，它將從 `a_code` 開始，迭代到 `a_code+26`（不包括26）。這是因為ASCII編碼 `'a'` 到 `'z'` 分別對應到97到122，因此迴圈將遍歷這個範圍。
4. `print(chr(i), end=' ')`：在迴圈內，這一行使用 `chr(i)` 將當前迴圈變數 `i` 轉換為相應的字符，並使用 `end=' '` 參數使所有字符在同一行上以空格分隔的方式輸出。這樣，迴圈將輸出小寫英文字母 `'a'` 到 `'z'`。

最終的輸出將是一個消息，顯示 `'a'` 的ASCII編碼，然後是小寫英文字母 `'a'` 到 `'z'`，每個字母之間以空格分隔。

</details>



## 2.3 基本運算

### 2.3.1 算術運算

以下是Python中用於運算的運算子：

| 運算子  | 說明                     | 舉例         |
|---------|--------------------------|--------------|
| `+`     | 加法                     | `3 + 2` -> `5`    |
| `-`     | 減法                     | `5 - 2` -> `3`    |
| `*`     | 乘法                     | `4 * 3` -> `12`   |
| `/`     | 除法                     | `8 / 2` -> `4.0`  |
| `//`    | 整數除法（取整數部分）  | `8 // 3` -> `2`   |
| `%`     | 取餘數                   | `8 % 3` -> `2`    |
| `**`    | 指數（幂運算）           | `2 ** 3` -> `8`   |
| `+=`    | 加法賦值                 | `a += 1`（相當於 `a = a + 1`） |
| `-=`    | 減法賦值                 | `b -= 2`（相當於 `b = b - 2`） |
| `*=`    | 乘法賦值                 | `c *= 3`（相當於 `c = c * 3`） |
| `/=`    | 除法賦值                 | `d /= 2`（相當於 `d = d / 2`） |

這些運算子用於執行基本的數學運算，並且可以用於不同的變數和數值。舉例說明了每個運算子的用法和效果。請注意，Python中的除法（`/`）通常返回浮點數結果，即使操作數是整數。如果需要整數結果，可以使用整數除法（`//`）。


```python
# 數值運算
10 + 4        # 14    
10 - 4        # 6  
10 * 4        # 40  
6 % 4         # 2
10 / 4        # 2.5  
10 // 4       # 2  
19 // 10      # 1  
10 ** 4       # 10000  

import math
math.ceil(10.1) 
```

#### round(): 四捨六入五成雙 

在 Python 中，`round()` 是一個常用於四捨五入的內建函式，但它的運作規則與我們在小學學的「四捨五入」不完全相同。Python 採用的是一種在科學與金融計算上更為精確的標準，稱為 **「銀行家捨入法」** (Banker's Rounding)，也常被稱為 **「四捨六入五成雙」**。

`round()` 函數的判斷邏輯可以清楚地分為以下三種情況：

1.  **小數部分 > 0.5**：無條件**向上進位**。
    * `round(3.7)` 的結果是 `4`。
    * `round(3.51)` 的結果是 `4`。

2.  **小數部分 < 0.5**：無條件**向下捨去**。
    * `round(3.2)` 的結果是 `3`。
    * `round(3.49)` 的結果是 `3`。

3.  **小數部分恰好等於 0.5**：這是最特殊的情況，會捨入到離它最近的**偶數** (Even Number)。
    * `round(2.5)` 的結果是 **`2`** (因為 `2` 是偶數)。
    * `round(3.5)` 的結果是 **`4`** (因為 `3` 是奇數，離它最近的偶數是 `4`)。
    * `round(4.5)` 的結果是 **`4`** (因為 `4` 是偶數)。

**規則對照表**

| 原始數字 | 規則判斷 | 結果 | 說明 |
| :--- | :--- | :-: | :--- |
| `5.2` | 小於 0.5 | `5` | 向下捨去。 |
| `5.8` | 大於 0.5 | `6` | 向上進位。 |
| `5.51` | 大於 0.5 | `6` | 向上進位。 |
| **`4.5`** | **等於 0.5** | **`4`** | 向最近的**偶數** (`4`) 捨去。 |
| **`7.5`** | **等於 0.5** | **`8`** | 向最近的**偶數** (`8`) 進位。 |

**為什麼要這樣設計？**

傳統的四捨五入法在處理大量數據時，因為 `0.5` 總是向上進位，會導致最終的總和系統性地偏高。

而「銀行家捨入法」將 `0.5` 的進位與捨去機率均分（一半的機率進位到偶數，一半的機率捨去到偶數），在對大量數據進行統計時，可以有效**減少累計的捨入誤差**，讓計算結果更接近真實值，因此在金融、科學等精密計算領域被廣泛採用。

#### 範例：算時間

```python
dist = 384400                           # 地球到月亮距離
speed = 1225                            # 馬赫速度每小時1225公里
total_hours = dist / speed              # 計算小時數
days = total_hours//24                  # 計算天
hours = total_hours % 24
print ('共需 {} 天 {} 小時'.format(days, hours))
```

結果：
```
共需 13.0 天 1.7959183673469283 小時
```

也可以使用 `divmod()`; `divmod()` 是一個函式，可以直接傳回商和餘數:

```python
# 利用 divmod
days, hours = divmod(total_hours, 24)   # 商和餘數
print ('共需 {} 天 {} 小時'.format(days, hours))

xmins = 60 * (hours - int(hours))
mins, secs = divmod(xmins, 60)
secs = 60 * (secs - int(secs))
h, m, s = int(hours), int(xmins), int(secs)
print ('共需 {} 天 {} 小時 {} 分 {} 秒 '.format(days, h, m, s))
```

結果：
```
共需 13.0 天 1 小時 47 分 45 秒 
```

### 2.3.2 字串運算

以下是 Python 中用於字串操作的運算子：

| 運算子  | 說明                 | 舉例                                           |
|---------|----------------------|------------------------------------------------|
| `+`     | 字串結合            | `"Hello, " + "world"` -> `"Hello, world"`    |
| `*`     | 重複字串            | `"abc" * 3` -> `"abcabcabc"`                  |
| `[]`    | 索引（提取字元）    | `"Python"[0]` -> `"P"`                       |
| `[:]`   | 切片（提取子字串）  | `"Python"[1:4]` -> `"yth"`                   |
| `len()` | 返回字串長度         | `len("Hello")` -> `5`                        |
| `in`    | 成員測試（是否包含）| `"e" in "Hello"` -> `True`                   |
| `not in`| 成員測試（是否不包含）| `"x" not in "Hello"` -> `True`              |

這些運算子和方法用於操作字串，可以實現字串的結合、提取、切片、測試包含等操作。舉例說明了每個運算子或方法的用法和效果。請注意，Python中的字串索引是從0開始的，而切片包括左側的索引但不包括右側的索引。

```python
# 字串運算
hello = "Hello" + ", " + "World"
print (hello)
name = "Nick"
print (name*3)
print ('N' in name)
print ('J' in name)
s = "0123456789"
print (s[5])   # 注意從 0 數起
print (s[3:6]) # 注意會印出 3~5, 不是 3~6 
```

```
Hello, World
NickNickNick
True
False
5
345
```

#### 字串函式

```python
hello = "Hello, Nick"
print ('hello: ', hello)
h1 = hello.upper()
h2 = hello.lower()
h3 = hello.replace('Hello','Hi')
print ('upper() 回傳: ', h1)
print ('lower() 回傳: ', h2)
print ('replace() 回傳: ', h3)
print ('hello 的值並沒有變, 依然是：', hello)
```
結果：
```
hello:  Hello, Nick
upper() 回傳:  HELLO, NICK
lower() 回傳:  hello, nick
replace() 回傳:  Hi, Nick
hello 的值並沒有變, 依然是： Hello, Nick
```

以下是一些常見的字串函式及其範例，以表格方式列出：

| 函式              | 描述                                    | 範例                                  |
|-------------------|-----------------------------------------|---------------------------------------|
| `upper()`         | 將字串轉換為大寫字母                | `"Hello, World!".upper()` 返回 `"HELLO, WORLD!"` |
| `lower()`         | 將字串轉換為小寫字母                | `"Hello, World!".lower()` 返回 `"hello, world!"` |
| `capitalize()`    | 將字串的首字母大寫                  | `"hello, world!".capitalize()` 返回 `"Hello, world!"` |
| `title()`         | 將字串中每個單字的首字母大寫        | `"hello, world!".title()` 返回 `"Hello, World!"` |
| `strip()`         | 移除字串兩端的空白字元              | `"   Hello, World!   ".strip()` 返回 `"Hello, World!"` |
| `rstrip()`        | 移除字串右側的空白字元              | `"   Hello, World!   ".rstrip()` 返回 `"   Hello, World!"` |
| `lstrip()`        | 移除字串左側的空白字元              | `"   Hello, World!   ".lstrip()` 返回 `"Hello, World!   "` |
| `replace(old, new)`| 將字串中的舊子字串替換為新子字串      | `"Hello, World!".replace("World", "Python")` 返回 `"Hello, Python!"` |
| `split(delimiter)`| 使用指定的分隔符將字串拆分為清單  | `"apple,banana,cherry".split(",")` 返回 `["apple", "banana", "cherry"]` |
| `join(iterable)`  | 將可迭代物件中的字串連接為一個字串 | `",".join(["apple", "banana", "cherry"])` 返回 `"apple,banana,cherry"` |
| `find(substring)`  | 查找子字串在字串中的位置（索引）     | `"Hello, World!".find("World")` 返回 `7` |
| `count(substring)` | 計算子字串在字串中出現的次數         | `"Hello, World, World!".count("World")` 返回 `2` |
| `startswith(prefix)`| 檢查字串是否以指定前綴開始     | `"Hello, World!".startswith("Hello")` 返回 `True` |
| `endswith(suffix)`  | 檢查字串是否以指定後綴結尾     | `"Hello, World!".endswith("World!")` 返回 `True` |

這些字串函式可用於對字串進行各種操作，如大小寫轉換、剪切、替換、拆分等。這些範例演示了每個函式的基本用法。

### 2.3.3 關係運算
以下是Python中用於執行關係運算的運算子、說明以及舉例的Markdown表格：

| 運算子  | 說明                     | 舉例              |
|---------|--------------------------|-------------------|
| `==`    | 等於                     | `3 == 3` -> `True`    |
| `!=`    | 不等於                   | `4 != 3` -> `True`    |
| `<`     | 小於                     | `2 < 5` -> `True`     |
| `>`     | 大於                     | `5 > 3` -> `True`     |
| `<=`    | 小於等於                 | `3 <= 3` -> `True`    |
| `>=`    | 大於等於                 | `4 >= 5` -> `False`   |

這些運算子用於比較兩個值的關係，並返回布林（Boolean）結果（True或False）。舉例說明了每個運算子的用法和效果。你可以使用這些運算子來構建條件語句，進行條件判斷和流程控制。

```python
# 關係運算
11 > 2            # True
11 >= 11          # True
11 != 2           # True
a, b = 11, 12
a >= b            # False
```

```python
## 邏輯運算
a = 11 > 2        # True
b = 1 > 9         # False
X = a and b       # True and False => False
Y = a or b        # True or False => True
Z = not a         # False
```

```python
isStudent = True
isKid = False
print (isStudent and isKid)  # False
print (isStudent or isKid)   # True
```

## 2.4 輸入與輸出

### 2.4.1 input 輸入

```python
# input 輸入
name = input("你的姓名? ")
print (name, type(name))
year = input("你的出生年? ")
print (year, type(year))

age = 2023-year
print ('{}的年齡是{}歲'.format(name, age))
```
互動與輸出：

```
你的姓名? Nick
Nick <class 'str'>
你的出生年? 2000
2000 <class 'str'>
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-11-b2ab0c782a60> in <cell line: 7>()
      5 print (year, type(year))
      6 
----> 7 age = 2023-year
      8 print ('{}的年齡是{}歲'.format(name, age))

TypeError: unsupported operand type(s) for -: 'int' and 'str'
```

這是因為我們忘了將 year 轉換為 int，以下做修改：

```python
# input 輸入
name = input("你的姓名? ")
print (name, type(name))
year = int(input("你的出生年? "))
print (year, type(year))

age = 2023-year
print ('{}的年齡是{}歲'.format(name, age))
```

```
你的姓名? Nick
Nick <class 'str'>
你的出生年? 2000
2000 <class 'int'>
Nick的年齡是23歲
```

#### 透過 split 做解析

如果我們要讀入一群數字，就需要將這個字串先切割（split），再轉成 int

```python
ages = input("輸入你和你哥哥的年齡，用 , 分隔")
```
> 12,23

這是後 ages 的值是 "12,23" 沒有辦法直接轉為整數，我們可以透過 `split()` 來做切割：

```python
a1, a2 = ages.split(",")
print (a1, a2)
age1 = int(a1)
age2 = int(a2)
print ('你們相差', (age2-age1), '歲')
```

執行結果：
```
12 23
你們 11 歲
```

#### eval() 

`eval()` 是一個更方便解析輸入數字的方法。我們不需要透過 split() 與 int 兩道程序：

```python
age1, age2 = eval(input("輸入你和你哥哥的年齡，用 , 分隔"))
print (age1, age2, type(age1))
```

當我們輸入 `12,23` 後，執行結果如下：

```
12, 23, int
```
可見得 `eval` 已經幫我解析與轉換型態了。

### 2.4.2 輸出

使用 print("輸出文字") 來輸出文字。如果提示字和變數要一起出現，可以用 `,` 來區隔。例如 `print('Your name is', name)`。但如果多個變數出現在一個句子中，單用 `,` 來連接會很麻煩。

字串和變數混合輸出的方法有：
- `%`
- `format()`

如下例：
```python
# 簡單的輸出
name = 'Nick'; age = 20

# 和字串的混合輸出: 比較麻煩的寫法
print ("Your name is", name, "and age is", age)

# 比較易懂的寫法：
# %s 表示 string; %d 表示 decimal; 透過 % 來連接與標示
print ("Your name is %s and age is %d" %(name, age))

# 透過 .format 來連接
print ("Your name is {} and age is {}".format(name, age))

# 先組裝字串再輸出
a1 = "Your name is %s and age is %d" %(name, age)
print (a1)    
a2 = "Your name is {} and age is {}".format(name, age)
print (a2)    
```

#### 排版

如果我們要印出多個浮點數字，
```python
a = [3.14159, 13.597, 4.12]

for x in a:
    print ('The number is', x, 'is that ok?')
```

輸出如下：
```
The number is 3.14159 is that ok?
The number is 13.597 is that ok?
The number is 4.12 is that ok?
```
排版有點凌亂，我們想取小數點下兩位就好：

```python
a = [3.14159, 13.597, 4.12]

for x in a:
    print ('The number is {:.2f}, is that ok?'.format(x))
```    

其中 `.2f` 表示小數點有兩位。輸出如下：
```
The number is 3.14, is that ok?
The number is 13.60, is that ok?
The number is 4.12, is that ok?
```

小數點並沒有對齊，我們想要固定整數部分一定有兩個空間，可以修改如下：
```python
a = [3.14159, 13.597, 4.12]

for x in a:
    print ('The number is {:5.2f}, is that ok?'.format(x))
```    

其中的 5 表示我們要用五個空格來表達該變數，所以3.14 和 4.12 前面會加上一個空格。輸出如下：
```
The number is  3.14, is that ok?
The number is 13.60, is that ok?
The number is  4.12, is that ok?
```

`:5.12f` 也可以改為 `0:5.12f`, 其中 0 表示後方第 0 個變數，也就是 x。當後方有多個變數時，我們可以把這個索引值加上。


### 2.4.3 逃脫字元

字串用 `" "` 來包裹起來，如果字串裡面包含 `"` 該如何處理？

Python中的逃脫字符（escape characters），它們的意義以及舉例：

| 逃脫字符 | 意義                                 | 舉例                            |
|----------|--------------------------------------|---------------------------------|
| `\n`     | 換行符（newline）                    | `"Hello,\nWorld!"` -> 換行       |
| `\t`     | 制表符（tab）                        | `"Name:\tJohn"` -> 用tab進行縮排 |
| `\\`     | 反斜杠（backslash）                  | `"C:\\Program Files"` -> 路徑   |
| `\'`     | 單引號（single quote）                | `"He said, \'Hello!\'"` -> 引號  |
| `\"`     | 雙引號（double quote）                | `"She said, \"Hi!\""` -> 引號    |

這些逃脫字符允許你在字串中插入特殊字符，例如換行符、制表符、引號等，而不會引起語法錯誤。當你需要在字串中表示這些特殊字符時，可以使用這些逃脫字符，使Python知道你的意圖。

例如，如果你想在字串中插入換行符，你可以使用`\n`，就像這樣：

```python
message = "Hello,\nWorld!"
```

這樣的設置將使`message`變數包含一個換行，將"Hello,"和"World!"分成兩行。


```python
# escape code
c1 = "he doesn't like apple"
c2 = 'he doesn\'t like apple'
c3 = 'first line\nsecond line'
c4 = "he doesn't like \tapple"
```

```
he doesn't like apple
he doesn't like apple
first line
second line
he doesn't like 	apple
```

#### 字串前綴

```python
c = r'first line\nsecond line'
print (c)
```

在這個Python程式碼中，`r` 不是一個逃脫字元，而是用於定義"raw string"（原始字串）的前綴。在原始字串中，逃脫字元不起作用，也就是說，字串中的反斜杠`\`會被當作普通字符對待，不會被解釋為逃脫序列。

輸出為

```
first line\nsecond line
```

### 2.4.4 字串相關函式

以下範例，注意 s 本身的值不會改變，這些函式呼叫後會回傳一個新的值。

```python
s = "I like Python"
r1 = s.lower()                 # 回傳 "i like python" (全轉小寫)
r2 = s.upper()                 # 回傳 "I LIKE PYTHON" (全轉大寫)
r3 = s.startswith('I')         # 回傳 True (檢查是否以 'I' 開頭)
r4 = s.endswith('python')      # 回傳 False (檢查是否以 'python' 結尾，大小寫需相符)
r5 = s.isdigit()               # 回傳 False (檢查字串是否只包含數字字元)
r6 = s.find('like')            # 回傳 2 (回傳子字串 'like' 的起始索引)
r7 = s.find('hate')            # 回傳 -1 (找不到子字串時回傳 -1)
r8 = s.replace('like', 'love') # 回傳 "I love Python" (字串替換)

s = "I like Python"

x1 = s.split(' ')              # 回傳 ['I', 'like', 'Python'] (以空格分割)
x2 = s.split()                 # 回傳 ['I', 'like', 'Python'] (預設以空白字元如空格、換行、Tab 分割)
x3 = s.split(',')              # 回傳 ['I like Python'] (字串中無 ','，回傳原字串為單一元素的串列)
```

### 2.4.5 讀寫文字檔

#### with 的用法

> 透過 print to file 建立一個 grade.txt 來記錄成績。

利用 with 區塊來做開檔，檔案建立後會自動關檔：
* w+ 表示是要覆寫 (write; w) 到檔案中，如果沒有檔案，就建立一個; 
* print (“要輸出的字”, file = f) 表示要輸出到檔案，不是螢幕。

```python
with open("grade.txt", 'w+') as f:
  print ('張三', file=f)
  print ('100, 20, 50', file=f)
  print ('李四', file=f)
  print ('90, 50, 100', file=f)
```

在上述程式碼中，`with` 的作用是創建一個上下文管理器，用於管理文件的讀取和寫入操作。這個上下文管理器確保在程式碼塊執行完成後，文件會被正確地關閉，即使在遇到錯誤或異常情況下也是如此。這是 `with` 語句的主要意義和作用。

執行後 grade.txt 的內容如下：
```
張三 
100, 20, 40
李四
90, 50, 100
```

#### readline() 
> 從 grade.txt 中讀檔案，計算後印出

`readline()` 會讀一行，因為也會把句末的換行 (\n) 也讀進來，所以這裡用 replace 將之置換掉。

```python
with open("grade.txt", "r") as f2:
   # st1 表示 student1  
   st1 = f2.readline().replace('\n', '')    # 張三  
   # 透過 eval() 來解析字串，轉換為數字  
   st1a, st1b, st1c = eval(f2.readline()) # 100, 20, 40
   # 計算平均  
   st1d = (st1a + st1b + st1c)/3
   print ("{} 的國英數成績是: {},{},{}, 平均為: {:5.1f}".format(st1, st1a, st1b, st1c, st1d))

   st2 = f2.readline().replace('\n', '')    # 李四  
   # 透過 eval() 來解析字串，轉換為數字  
   st2a, st2b, st2c = eval(f2.readline()) # 90, 50, 100
   # 計算平均  
   st2d = (st2a + st2b + st2c)/3
   print ("{} 的國英數成績是: {},{},{}, 平均為: {:5.1f}".format(st2, st2a, st2b, st2c, st2d))
```



## 2.5 程式錯誤

以下是使用Markdown表格方式呈現的程式碼錯誤類型的說明：

| 錯誤類型          | 意義                                         | 舉例                                  |
|-------------------|----------------------------------------------|---------------------------------------|
| 語法錯誤（Syntax Error） | 程式碼不符合語法規則，無法編譯或解釋 | 忘記冒號、未結束的引號、括號不匹配     |
| 執行錯誤（Execution Error） | 程序在運行時發生問題，可能是無效輸入、文件不存在等 | 除以零、訪問不存在的文件、索引越界    |
| 邏輯錯誤（Logic Error）   | 程式碼在語法上正確，但其邏輯或行為錯誤    | 錯誤的算法、不正確的邏輯判斷、變數值錯誤 |

這個表格提供了對每種錯誤類型的簡要說明，並提供了相應的示例。這有助於開發者更容易地理解不同錯誤的性質和可能的原因。

```python
# syntax error
radius = int(input("The radius? ")
area = radius ** radius * 3.14
print (area)
```

`input` 右邊少了一個 `)`, Python 就不認得這樣的語法了，是個語法錯誤。

```python
# run time error if you input 1.1
radius = int(input("The radius? "))
area = radius ** radius * 3.14
print (area)
```

上面的程式沒有錯誤，但是如果我們輸入 "1.1", int() 並沒有辦法把字串的 1.1 轉換為 int, 所以發生執行上的錯誤。我們改用 float() 來轉換：

```python
# logic error
# if you input 1 or 2, you'll not find it
radius = float(input("The radius? "))
area = radius ** radius * 3.14
print (area)
```

上面的程式雖然不會有執行的錯誤了，但有語法的錯誤：`**` 代表的是次方，我們本來要寫的是 `radius*radius`。如果測試時 radius 的值是 1或2, 還不會發現錯誤呢。修改如下：


```python
# bad code: not easy to maintain
radius = float(input("The radius? "))
area = radius * radius * 3.14
print (area)
```

上面的程式雖然對了，但可以改得更好，我們用 PI 來代表 3.14, 這樣以後如果我們想要更精準的計算面積，想用 3.14159 來代表 PI，就不用改太多。

```python
# much better
PI = 3.14159
radius = float(input("The radius? "))
area = radius * radius * PI
print (area)
```

輕鬆一下
> :sunglasses: 遇到錯誤千萬不要只是註解掉該錯誤，要認真除錯啊



## 2.6 程式的註解

以下是已移除範例的Python註解方式的表格：

| 註解方式            | 語法               | 說明                                                         |
|---------------------|--------------------|--------------------------------------------------------------|
| 行內註解（Inline Comment） | `#`                | 在一行程式碼中使用 `#` 來添加註解。註解位於程式碼行的尾部。     |
| 單行註解（Single-Line Comment） | `#` 開頭           | 使用 `#` 在一行中添加單行註解。通常在程式碼行上方。             |
| 多行註解（Multi-Line Comment） | `'''` 或 `"""` 包裹  | 使用三引號 `'''` 或 `"""` 包裹多行註解，通常用於多行說明。 |


```python
'''
本程式用來排序一群資料
這群資料的產生是隨機產生的
透過氣泡排序法來排序

by Nick Hsueh, 2018/1/1
'''

import random
a = []

# 單行註解：隨機的產生100個數字
for i in range(100):
    a.append(random.randint(1,100))
print(a)     # 行內註解：印出原資料

s = len(a)   # 資料大小
r = s-1      # 回合數

for i in range(1, r+1):
    print('Round', i)
    for j in range(0, s-i-1):
        
        # 將 a[j] 與 a[i] 的資料對調
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            
    print(a) # 印出排序後的資料
```

## 2.7 程式練習

> [!NOTE]
> :basketball: Ex01 OJ 面積與周長
> 描述：
> 輸入直徑，計算出面積與周長，並輸出至小數點下兩位。注意 pi 請用 3.14 來計算。
>
>
> | 資料           | 範例 1        | 範例 2        |
> |----------------|--------------|--------------|
> | 輸入-直徑     | 2            | 10           |
> | 輸出-面積     | 3.14         | 78.5         |
> | 輸出-周長     | 6.28         | 31.4         |
>
>
> Code:
> ```python
> d = int(input('')) # 此行勿改。d 為直徑
> a =  # 面積
> p =  # 周長
> print (a) # 此行勿改
> print (p) # 此行勿改
> ```

<details>
<summary>點擊查看參考解答</summary>

```python
d = int(input('')) # 此行勿改。d 為直徑
a =  round((d/2) **2 * 3.14, 2)  # 面積
p =  round(d * 3.14, 2)  # 周長
print (a) # 此行勿改
print (p) # 此行勿改
```

</details>


> [!NOTE]
> OJ 星期幾
> 已知某個月的一號是星期1, 輸入該月的日期，請回答是星期幾。注意若為星期日，則為星期 7，也就是答案落在1,2,... 7 其中一個值。

<details>
<summary>點擊查看參考解答</summary>

```python
day = int(input(''))
# 1號是星期1，(day - 1) % 7 結果為 0~6，+1 即為 1~7
ans = (day - 1) % 7 + 1
print(ans)
```

</details>


> [!NOTE]
> OJ 溫度轉換
>
> 設計攝氏溫度和華氏溫度的轉換。輸入攝氏輸出華氏。
> 華氏溫度 = 攝氏溫度 * ( 9 / 5 ) + 32 (取小數點下兩位)
>
> ```python
> Code:
> c = int(input('')) # 此行勿改。c 為攝氏
>
> # write your code here
>
> print (f) # 此行勿改。f 為輸出之華氏
> ```

<details>
<summary>點擊查看參考解答</summary>

```python
c = int(input('')) # 此行勿改。c 為攝氏

f = round(c * (9 / 5) + 32, 2)

print (f) # 此行勿改。f 為輸出之華氏
```

</details>


> [!NOTE]
> OJ 計算距離
>
> 兩個座標的距離，是各自 x, y 的座標差的平方和再開根號：
>
> ```python
> Hint：開根號，可使用 ** 0.5 來做
>
> Code:
> x1, y1 = eval(input('')) # 此行勿改。x1, y1 是第一個座標
> x2, y2 = eval(input('')) # 此行勿改。x2, y2 是第二個座標
>
> d  # d 為兩個座標的距離
>
> print (d) # 此行勿改
> ```

<details>
<summary>點擊查看參考解答</summary>

```python
x1, y1 = eval(input('')) # 此行勿改。x1, y1 是第一個座標
x2, y2 = eval(input('')) # 此行勿改。x2, y2 是第二個座標

d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5  # d 為兩個座標的距離

print (d) # 此行勿改
```

</details>
