# Nhap thong tin benh nhan va kiem tra du lieu
name_patient=input("Nhap ten benh nhan: ")
if not name_patient:
    print("Ten nguoi dung khong duoc de trong")

year = int(input("Nhap nam sinh: "))
if year < 1900 and year >2026:
    print("Nam sinh phai nam trong khoang [1900-2026]")

day_of_sick= int(input("Nhap vao so ngay bi benh: "))
if day_of_sick < 0 :
    print("So ngay bi benh phai >=0")

temperature_patient=float(input("Nhap vao nhiet do co the: "))
if temperature_patient <30 and temperature_patient > 45:
    print("Nhiet do phai nam trong khoang [30-45]")

price_patient = float(input("Nhap chi phi kham: "))
if price_patient <0 :
    print("Chi phi kham phai > 0")

# Tinh toan thong tin 
age = 2026 - year
surchange = price_patient * 0.1
total_cost = price_patient+surchange

# Phan loai tinh trang suc khoe
status =""
if temperature_patient > 38 and day_of_sick > 3:
    status="Nguy hiem"
    print(status)
elif temperature_patient > 38:
    status="Sot cao"
    print(status)
elif temperature_patient > 37.5:
    status="Sot nhe"
    print(status) 
else:
    status="Binh thuong"  
    print(status) 

# Danh gia muc do uu tien
prioritize =""
if status == "Nguy hiem":
    if age > 60:
        prioritize="Cap cuu"
        print(prioritize)
    else:
        prioritize="Uu tien cao"
        print(prioritize)
else:
    prioritize="Binh thuong"
    print(prioritize)

# Danh gia muc chi phi
priority ="Cao" if total_cost > 500000 else "Thap"

# In ket qua
print("-----Ket qua----")
print(f"Ten: {name_patient}")
print(f"Tuoi: {age}")
print(f"Nhiet do: {temperature_patient}")
print(f"So ngay benh: {day_of_sick}")

print(f"Tinh trang: {status}")
print(f"Muc do uu tien: {prioritize}")

print(f"Tong chi phi: {total_cost}")
print(f"Muc chi phi: {priority}")








