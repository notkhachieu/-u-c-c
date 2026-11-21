#Bài 1 
n = float(input("Nhập số thực n: "))
print ("Số thực 2n là: ", n*2)

#Bài 2 
a = float(input("Nhập vào chiều rộng: "))
b = float(input("Nhập vào chiều dài: "))
if a*b - 3.14*(1**2) < 0: 
     print("Giá trị diện tích phần trồng cỏ là âm, vui lòng nhập lại chiều dài và chiều rộng")
else:
     print("Diện tích phần trồng cỏ là: ", round(a*b - 3.14*(1**2),2))

#Bài 3 

letter = input("Nhập vào một ký tự: ")
if letter.isupper() : 
     print("Ký tự viết thường của bạn là: ", letter.lower())
else : 
     print("Ký tự viết hoa của bạn là: ", letter.upper())

#Bài 4 

character = input("Nhập vào một kí tự: ")

if character.isalpha() :
     print({character} + " là một chữ cái")
else: 
     print({character} + " không phải là một chữ cái")

#Bài 5 : 

letter = input("Nhập vào một ký tự in hoa: ")
if letter == "A" or letter == "a" :
    print("Không có ký tự nào đứng trước A")

else : 
    print("Ký tự đứng trước", letter, "là", chr(ord(letter) - 1))

#Bài 6:

a,b,c = map(float, input("Nhập vào 3 cạnh của tam giác: ").split())
p = (a+b+c)/2
if a+b>c and a+c>b and b+c>a:
     print ("Diện tích tam giác là: ", round((p*(p-a)*(p-b)*(p-c))**0.5,1))
else:
     print("Không phải là 3 cạnh của tam giác.")

#Bài 7:

chuỗi = input("Nhập vào một chuỗi: ")
print("Vị trí số 5 và 9 trong chuỗi là: ", chuỗi[4], "và", chuỗi[8])

#Bài 8:
a = input("Tên chủ hộ: ")
b = float(input("Nhập vào số điện tháng trước : "))
c = float(input("Nhập vào số điện tháng này : "))
if 0 <= c-b <= 50:
     print("Số tiền điện phải trả là: ", (c-b)*1984*1.08)
elif 50 < c-b <= 100 :
     print("Số tiền điện phải trả là: ", (50*1984 + (c-b-50)*2050)*1.08)
elif  100 < c-b <=200 :
     print("Số tiền điện phải trả là: ", (50*1984 + 50*2050 + (c-b-100)*2380)*1.08)
elif 200 < c-b <=300 :
     print("Số tiền điện phải trả là : ", (50*1984 + 50*2050 + 100*2380 + (c-b-200)*2998)*1.08)
elif 300 < c-b <= 400 :
     print("Số tiền điện phải trả là: ", (50*1984 + 50*2050 + 100*2380 + 100*2998 + (c-b-300)*3350)*1.08)
elif 400 < c-b :
        print("Số tiền điện phải trả là: ", (50*1984 + 50*2050 + 100*2380 + 100*2998 + 100*3350 + (c-b-400)*3460)*1.08)


##BÀI TẬP BỔ SUNG 
#bài 1 : 

a = int(input("Nhập vào số a: "))
if a % 2 == 0 :
        print("Số a là số chẵn")
else : 
        print("Số a là số lẻ")

#Bài 2 :

a = int(input("Nhập vào số nguyên a: "))
if a % 5 == 0 and a % 10 == 0 :
     print("True")
else : print("False")

#Bài 3 :

a = int(input("Nhập vào số nguyên a: "))
if a % 3 == 0 and a % 5 == 0 :
     print("True")
else : print("False")

#Bài 4 :

a = int(input("Nhập vào năm sinh của bạn : "))

if a - 2026 < 18 :
     print("Chưa đủ tuổi đi bầu cử.")
else : print("Đi bầu đi.")

#Bài 5 :
a,b = map(float, input("Nhập vào 2 số a và b: ").split())
if a > b :
     print("Số lớn hơn là: ", a)
elif a < b :
     print("Số lớn hơn là: ", b)
else : print("Hai số bằng nhau.")

#Bài 6:
letter = input("Nhập vào một ký tự: ")
if letter.isnumeric() :
     print ("Đây là một chữ số")
else : print("Đây là một chữ cái")

#Bài 7 : 
Diem = float(input("Nhập vào điểm của bạn: "))
if Diem >=8 : print("Bạn đạt loại giỏi")
elif 6.5 <= Diem < 8 : print("Bạn đạt loại khá")
elif 5 <= Diem < 6.5 : print("Bạn đạt loại trung bình")
else : print("Bạn đạt loại yếu")

#Bài 8 :
year = int(input("Nhập vào năm: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
     print("Năm", year, "là năm nhuận")
else : print("Năm", year, "không phải là năm nhuận")

#Bài 9 :

#Bài 10:
Diem_thi = float(input("Nhập vào điểm thi: "))
if Diem_thi >= 4 : print ("Bạn đã qua môn")
else : print("Học lại")

#Bài 11 : giống bài 4

