#Bài 1:
a,b = map(float, input("Nhập chiều dài và chiều rộng của hình chữ nhật: ").split())
print("Diện tích hình chữ nhật là: ", a*b)
print("Chu vi hình chữ nhật là: ", (a+b)*2)

#Bài 2 :

R = float(input("Nhập bán kính hình tròn: "))
print("Diện tích hình tròn là: ", 3.14*R**2)
print("Chu vi hình tròn là: ", 2*3.14*R)

#Bài 3 :

a,b,c = map(float, input("Nhập 3 cạnh của tam giác: ").split())
if a+b>c and a+c>b and b+c>a:
    
    if a==b and b==c:
        print("Tam giác đều")
    elif a==b or b==c or a==c:
        print("Tam giác cân")
    elif a == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print("Tam giác vuông")
    else : print("Tam giác thường")
else:
    print("3 cạnh không tạo thành tam giác")

#Bài 4 

a,b = map(int, input().split())
if a == 0 and b != 0 :
    print("vô nghiệm")
elif a == 0 and b== 0 :
    print("vô số nghiệm")
elif a != 0 and b == 0 :
    print("vô số nghiệm")
else : 
    print(-b/a)

#Bài 5 :
a,b,c = map(int,input().split())
delta = b**2 - 4*a*c 
if delta < 0 :
        print("Vô nghiệm")
elif delta == 0 :
        print("Pt có nghiệm duy nhất là : ", -b/2*a)
else :
        print("Pt có 2 nghiệm phân biệt là", (-b+delta**(1/2))/2*a ,"và", (-b-delta**(1/2))/2*a)
#Bài 6 

a,b,c,d = map(int, input().split())
max = a
if a < b and b > c and b >d :
     max = b
     print(max)
elif c > b and c > a and c >d :
     max = c 
     print(max)
elif d > c > b > a:
     max = d
     print(max)
else :
     print(a)

#Bài 7 

a,b,c,d = map(int, input().split())
if b < a and b < c and b < d :
     print(b)
elif c < a and c < b and c < d :
     print(c)
elif d < a and d < b and d < c : 
     print(d)
else :
     print(a)

#Bài 8 

a,b,m,c,d,n = map(int, input().split())
if a == c :
     print("Phương trình có nghiệm là: ", (m-n)/(b-d), "và", m/a - (b*(m-n)/(b-d))/a )
else :
     print("Phương trình có nghiệm là: ", (m*c/a)/(b*c/a - d), "và", ())


#Bài 9 

time = (int(input()))
if 0 < time <= 60 :
     print(time, "giây")
elif 60 < time < 3600 :
     phut = time // 60
     giay = time - phut*60
     print(phut,"phút", giay, "giây")
elif time < 0 :
     print("Vô lí")
else : 
     gio = time // 3600
     phut = (time-gio*3600)//60
     giay = (time-gio*3600-phut*60)
     print(gio,"giờ",phut,"phút",giay,"giây")

#Bài 10

R = int(input())
x,y = map(int,input().split())
a*a = x**2 + y**2
if R*R == a*a :
     print("Điểm nằm trên đường tròn")
elif R*R > a*a :
     print("Điểm nằm trong đường tròn")
else :
     print("Điểm nằm ngoài đường tròn")

#Bài 11

x,y = map(int,input().split())
print(x**y)