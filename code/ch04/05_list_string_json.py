# 05_list_string_json.py - JSON 轉換與字串切分/合併 (split & join)
import json

# 1. json.loads() 將列表字串轉換為 Python list 物件
json_str = "[60, 78, 100]"
parsed_list = json.loads(json_str)
print('解析後的 List 物件:', parsed_list)
print('型態:', type(parsed_list))

# 2. 字串 split 與 join 操作
city_string = "Taichung Taipei Kaoshiung"
# 切割為 list
city_list = city_string.split()
print('切割後的列表:', city_list)

# 以特定符號連接 list 元素
joined_str_1 = '-'.join(city_list)
joined_str_2 = ' * '.join(city_list)
print("join '-' 連接:", joined_str_1)
print("join ' * ' 連接:", joined_str_2)
