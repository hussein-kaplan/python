# --- hussein kaplan --- حسين قبلان
# استدعاء المكتبات المطلوبة
import os
import os.path
from instagrapi import Client
import json

# --- قراءة ملف تسجيل الدخول 
filescheck = os.path.exists("credential.json")
def write_file(data, path_file, default=None):
    from pathlib import Path
    path_user = Path(path_file)
    path_user.parent.mkdir(exist_ok=True)
    with open(path_file, 'w', encoding='utf8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=True, default=default)

# --- التاكد من وجود الملف 
if filescheck == True:
    # --- فتح ملف اليوزرات
    if os.stat("username.txt").st_size == 0:
        username = input("enter User name :")
        f = open("username.txt", "a")
        f.write(username)
        f.close()
    f = open("username.txt", "r")
    for x in f:
        os.system("start /B start cmd.exe @cmd /k python stories.py "+ str(x))
#  --- اذ لم يجد ملف تسجيل الدخول سيطلب منك تسجيل دخول جديد
else :
    IG_CREDENTIAL_PATH = "credential.json"
    acountslist = input("input account username : ")
    password = input("input account password :")


    print(acountslist)
    IG_USERNAME = acountslist
    IG_PASSWORD = password
        
    cl = Client()
    cl.login(IG_USERNAME, IG_PASSWORD)
    write_file(cl.get_settings(), IG_CREDENTIAL_PATH)
    if os.stat("username.txt").st_size == 0:
        # --- فتح ملف اليوزرات
        username = input("enter User name :")
        f = open("username.txt", "a")
        f.write(username)
        f.close()
    f = open("username.txt", "r")
    for x in f:
        os.system("start /B start cmd.exe @cmd /k python stories.py "+ str(x))