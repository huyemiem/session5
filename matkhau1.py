pass1=input("Nhap mat khau:")

if pass1.isalpha():
    print('yeu cau nhap lai')

elif len(pass1)<=8:
    print('yeu cau nhap lai')

else:
    print ("nhap mat khau thanh cong")