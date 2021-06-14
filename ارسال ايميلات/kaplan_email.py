import smtplib # --- استدعاء المكتبات المهمة
import csv # --- استدعاء المكتبات المهمة
from email.message import EmailMessage # --- استدعاء المكتبات المهمة
youremail = input("Enter your email to login :") # --- ايميل الحساب لتسجيل دخول
yourpassword = input("Enter your password to login :") # --- كلمة سر الحساب
subject = input("Enter the subject :") # --- عنوان الايميل
body = input("Enter the message :") # --- رسالة الايميل

server = smtplib.SMTP_SSL("smtp.gmail.com", 465) # --- عمل سيرفر محلي   
server.login(youremail, yourpassword) # --- تسجيل الدخول
with open("emails.csv", newline="") as csvfile: # --- قراءة الايميلات من الملف 
    spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
    count=0
    for email in spamreader: # --- عمل لوب لايميلات داخل الملف
        count +=1
        print ("send email --> " + str(count)) # --- كتابة عدد الايميلات
        msg = EmailMessage() # --- كتابة الرسالة
        msg['Subject'] = subject # --- العنوان
        msg['From'] = youremail # --- تم الارسال من
        msg['to'] = email # --- تم الارسال الى 
        msg.set_content(body) # --- محتوى الرسالة
        server.send_message(msg) # --- ارسال الرسالة
server.quit() # --- اغلاق البرنامج
print("Emails sent successfully") # --- طباعة رسالة نجاح الارسال