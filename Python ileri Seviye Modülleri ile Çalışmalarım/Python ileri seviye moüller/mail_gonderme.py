import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys 


mesaj = MIMEMultipart()

mesaj["From"] = "mustafaklc2434@gmail.com"

mesaj["To"] = "kilicmustafa.tr@gmail.com"

mesaj["Subject"] = "Mail Baslıgı"

yazi = """ 

Smtp ile mail gönderiyorum

Mustafa Kılıç

"""

mesaj_govdesi = MIMEText(yazi ,"plain")
mesaj.attach(mesaj_govdesi)

try : 

    mail = stmplib.STMP("smtp.gmail.com",587)
    mail.ehle()
    mail.starttls()
    mail.login("" , "")
    mail.sendmail(mesaj["From"] ,mesaj["TO"] ,mesaj.as_string())

    print("Mesaj başarılı bir şekilde gönderildi")

except : 
    
    sys.stderr.write("Bir sorun oluştu !")
    sys.stderr.flush()

    