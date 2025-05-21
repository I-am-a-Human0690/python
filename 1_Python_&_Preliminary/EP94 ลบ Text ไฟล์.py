#ลบไฟล๋ txt
import os
#os.remove("EP94.2.txt")
if os.path.exists("EP94.2.txt"):
    os.remove("EP94.2.txt")
    print("ลบแล้ว")
else:
    print("หาไฟล์ไม่เจอ")