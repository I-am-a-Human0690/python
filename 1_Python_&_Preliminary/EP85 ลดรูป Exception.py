#Exeption
#ให้บอกปัญหาเอง หรือ การเขียนลดรูป
# try:
#     a=int(input(":"))
#     b=int(input(":"))
#     c=a/b
#     print(c)
# except Exception as e:
#     print(e)

try:
    a=int(input(":"))
    b=int(input(":"))
    c=a/b
    print(c)
except ValueError:
    print('sss')