# 07_set_operations.py - 集合 Set 的宣告、交集/聯集/差集與 CRUD

# 1. 宣告與去重
baseball = ['Nick', 'Albert', 'Jie']
piano = ['Nick', 'Doris']
highGrade = ['Nick', 'Doris', 'Anna']

baseballSet = set(baseball)
pianoSet = set(piano)

# 聯集 (Union) - 兩社團總參與人數
community = baseballSet | pianoSet
print('棒球社或鋼琴社總名單 (聯集):', community)

# 交集 (Intersection) - 社團成員中獲得高分者
communityAndHighGrade = community & set(highGrade)
print('社團成員中獲得高分者 (交集):', communityAndHighGrade)

# 差集 (Difference) - 高分但沒有參加社團者
highGradeButNoCommunity = set(highGrade) - community
print('高分但沒參加社團者 (差集):', highGradeButNoCommunity)

# 2. 增修刪查 (CRUD)
basketball = set()
# 增
basketball.add('Alex')
basketball.add('Alex')  # 重複新增自動忽略
basketball.add('Nick')
print('新增球員後:', basketball)

# 刪
basketball.remove('Nick')  # 正常刪除
# basketball.remove('Jonathan') # 刪除不存在者會報 KeyError
basketball.discard('Peter')    # 刪除不存在者不會報錯
print('刪除球員後:', basketball)

# 查
print("是否有 'Alex' 在球隊中:", 'Alex' in basketball)
