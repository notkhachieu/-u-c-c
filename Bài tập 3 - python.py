#W3A2 

a,b = map(int, input("Nhập 2 số: ").split())
a,b = b,a
print("Sau khi hoán đổi: a = ", a, "b = ", b)

#W3A3 

n = int(input("Nhập số nguyên dương n: "))
if n&(n-1) == 0 :
    print(n, "là số nguyên dương là lũy thừa của 2")
else : print(n, "không là số nguyên dương là lũy thừa của 2")

#W3A4

m,n = map(int, input().split())
print(int(m/n))

#W3A5 

m,n = map(int, input().split())
print(int(m/n + 0.5))

#W3A6 

n = int(input("Nhập số nguyên dương n: "))
if n%2 == 0 :
    print("Even")
else : print("Odd")

#W3A7 

a,b = map(int, input().split())
if a < 0 and b < 0 :
    print("Yes")
else : print("No")

#W3A8 

a,b = map(input().split())
if a > b :
    print("Yes")
else : print("No")

#W3A9 

a,b,c = map(int, input().split())
if a + b > c and a + c >b and b + c > a :
    print("Yes")
else : print("No")

#W3A10

a,b,c,d = map(int, input().split())
Max = a 
if Max < b : Max = b
elif Max < c : Max = c
else : Max = d
print(Max) 

#W3A11

a,b,c = map(int, input().split())
if a == b and b == c :
    print("Tam giác đều")
elif a == b or b == c or a==c :
    print("Tam giác cân")
elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2 :
    print("Tam giác vuông")
elif a**2 < b**2 + c**2 and b**2 < a**2 + c**2 and c**2 < a**2 + b**2 :
    print("Tam giác thường")
else : print("3 cạnh không tạo thành tam giác")

#W3A12 

year = int(input())
if year%4 == 0 and year%100 != 0 or year%400 == 0 :
    print(year, "là năm nhuận")
else : print(year, "không là năm nhuận")

#W3A14

a,b = map(int, input().split())
if a == 0 and b != 0 :
    print("Vô nghiệm")
elif a == 0 and b == 0 :
    print("Vô số nghiệm")
elif a!= 0 and b != 0 :
    print(-b/a)
else :
    print("0")

#W3A15 

n = float(input("Điểm trung bình: "))
if n >= 8 :
    print("Giỏi")
elif 6.5 <= n < 8 :
    print("Khá")
elif 5 <= n < 6.5 :
    print("Trung bình")
else :
    print("Yếu")