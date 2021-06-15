# Hussein kaplan - حسين قبلان
# --- يجب عليك تحميل المكتبة اولا عبر الامر 
# pip install xmltodict
import json # --- استدعاء مكتبة  للتعامل مع ملفات ال 
import xmltodict # --- استدعاء مكتبة التحويل

with open('data.xml') as xml_file: # --- xml فتح ملف ال 
    print("Xml جاري قراءة ملف")
    get_data = xmltodict.parse(xml_file.read()) # --- قراءة محتويات الملف وتحويله
    print("Xml جاري اغلاق ملف")
    xml_file.close() # --- الان نغلق الملف بعد قراءة المحتويات
    print("جاري تحويل صيغة البيانات")
    json_trans = json.dumps(get_data) # --- Json نقوم بتحويل البيانات الى صيغة 

    with open('output.json', 'w') as json_file: # --- Json بفتح ملف ال 
        print("json جاري قراءة ملف")
        json_file.write(json_trans)  # --- كتابة البيانات في الملف
        print("Json جاري اغلاق ملف")
        json_file.close() # --- اغلاق الملف
    print("تم تحويل الصيغة")
