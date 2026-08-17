class Car:

    kind = '燃油車'                 # 類別變數
    travel = []                    # 類別變數 

    def __init__(self, car_id):
        self.car_id = car_id       # 物件變數

print ('類別變數的值：', Car.kind, Car.travel) # 燃油車 []
c1 = Car('c1')  
c2 = Car('c2')  
print (c1.car_id, c1.kind)  # c1 燃油車
print (c2.car_id, c2.kind)  # c2 燃油車

print ('\n修改一些 c1 的類別變數，c1 變成 電動車 且加上 車架')
c1.kind = '電動車'             
c1.travel.append('車架')

print (Car.kind, Car.travel)            # 燃油車 ['車架']
print (c1.car_id, c1.kind, c1.travel)   # c1 電動車 ['車架']
print (c2.car_id, c2.kind, c2.travel)   # c2 燃油車 ['車架']

print ('\n現在直接修改 Car 的類別變數')
Car.kind = '油電混合車'
Car.travel.append('旅行支架')
print (c1.car_id, c1.kind, c1.travel)   # c1 電動車 ['車架', '旅行支架']
print (c2.car_id, c2.kind, c2.travel)   # c2 油電混合車 ['車架', '旅行支架']