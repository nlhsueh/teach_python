# 02_class_vs_instance_attrs.py - 類別屬性 (Class Attribute) 與實例屬性 (Instance Attribute) 的區別

class Car:
    # 1. 類別屬性 (所有物件共享一份記憶體空間)
    kind = '燃油車'
    
    def __init__(self, car_id):
        # 2. 實例屬性 (每個物件擁有獨立的空間)
        self.car_id = car_id

c1 = Car('Tesla-01')
c2 = Car('Toyota-02')

print("=== 初始狀態 ===")
print("Car 類別屬性 kind:", Car.kind)
print("c1 的 kind:", c1.kind, "| ID:", c1.car_id)
print("c2 的 kind:", c2.kind, "| ID:", c2.car_id)

# 修改類別屬性，會影響所有未遮蔽此屬性的實例
Car.kind = '電動車'
print("\n=== 修改類別屬性後 ===")
print("Car 類別屬性 kind:", Car.kind)
print("c1 的 kind (隨之改變):", c1.kind)
print("c2 的 kind (隨之改變):", c2.kind)

# 在 c1 實例上自訂一個與類別屬性同名的實例屬性 (遮蔽/Shadowing)
c1.kind = '複合動力車'
print("\n=== 在 c1 實例單獨指定同名屬性後 (發生遮蔽) ===")
print("Car 類別屬性 kind:", Car.kind)
print("c1 的 kind (已被實例屬性覆蓋):", c1.kind)
print("c2 的 kind (依然跟隨類別屬性):", c2.kind)
