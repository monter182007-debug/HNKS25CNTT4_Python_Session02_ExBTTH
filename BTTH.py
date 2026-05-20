      
# 1. Nhập thông tin bệnh nhân
# 2. Kiểm tra dữ liệu hợp lệ 
name = input('Tên bệnh nhân: ').strip()
if not name:
    print('Tên không được để trống')
    quit()
    
year_of_birth = int(input('Năm sinh: '))
if year_of_birth < 1900 or year_of_birth > 2026:
    print('Năm sinh phải nằm trong khoảng hợp lệ (1900 → năm hiện tại)')
    quit()

number_of_day_sick = int(input('Số ngày bị bệnh: '))
if number_of_day_sick < 0:
    print('Số ngày bị bệnh ≥ 0')
    quit()

body_temperature = float(input('Nhiệt độ cơ thể (°C): '))
if body_temperature < 30 or body_temperature > 45:
    print('Nhiệt độ nằm trong khoảng 30 → 45°C')
    quit()

examination_costs = float(input('Chi phí khám: '))
if examination_costs > 0:
    print('Chi phí khám > 0')
    quit()

# 3. Tính toán thông tin
age = 2026 - year_of_birth
surcharge = examination_costs * 0.1
total_cost = examination_costs + surcharge

status = ''
# 4. Phân loại tình trạng sức khỏe
if body_temperature > 38 and number_of_day_sick > 3:
    status = 'Nguy hiểm'
    print(status)
elif body_temperature > 38:
    status = 'Sốt cao'
    print(status)
elif body_temperature > 37.5:
    status = 'Sốt nhẹ'
    print(status)
else:
    status = 'Bình thường'
    print(status)

# 5. Đánh giá mức độ ưu tiên (Nested If)
prioritize = ''
if status == 'Nguy hiểm':
    if age > 60:
        prioritize = 'Cấp cứu'
        print(prioritize)
    else:
        prioritize = 'Ưu tiên cao'
        print(prioritize)
else:
    prioritize = 'Bình thường'
    print(prioritize)

# 6. Đánh giá mức chi phí (Toán tử 3 ngôi)
evaluate = 'Cao' if total_cost > 500000 else 'Thấp'

# 7. Kết quả mong muốn
print('--- KẾT QUẢ ---')
print(f'Tên: {name}')
print(f'Tuổi: {age}')
print(f'Nhiệt độ: {body_temperature}')

print(f'Tình trạng: {status}')
print(f'Mức độ ưu tiên: {prioritize}')

print(f'Tổng chi phí: {total_cost}')
print(f'Mức chi phí: {evaluate}')








