# 09_dict_advanced.py - 字典推導式、字典合併運算子與 JSON 轉換
import json

# 1. 字典合併與更新 (Python 3.9+)
dict1 = {'apple': 10, 'banana': 20}
dict2 = {'banana': 30, 'cherry': 40}

# | 聯集運算 (不改變原字典，重複 key 則以後者為準)
merged_d = dict1 | dict2
print('合併後字典 merged_d:', merged_d)
print('原 dict1 未改變:', dict1)

# |= 更新運算 (原地修改)
dict1 |= dict2
print('dict1 原地更新後:', dict1)

# 2. 現代 zip 與 strict=True (Python 3.10+)
std = ['nick', 'john', 'mac']
grades = [100, 90, 80]

# zip 轉 dict
std_grade_dict = dict(zip(std, grades, strict=True))
print('透過 zip 與 strict=True 轉換字典:', std_grade_dict)

# 字典推導式 (Dict Comprehension)
dict_comp = {k: v for k, v in zip(std, grades, strict=True)}
print('字典推導式輸出:', dict_comp)

# 3. JSON 格式字串的 load 與 dump
gStr = '{"eng": 60, "math": 78, "phy": 100}'
# JSON str -> Dict
gDict = json.loads(gStr)
print('loads 轉換後的 dict 物件:', gDict)

# Dict -> JSON str
output_json = json.dumps(gDict)
print('dumps 輸出 JSON 字串:', output_json)
