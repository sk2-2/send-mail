
import smtlib
a=smtlib.SMTP("smtp.gmail.com:587")
a.starttls()
a.login("shrikrishan.khandelwal@gmail.com","jakiekerry")
a.sendmail("shrikrishan.khandelwal@gmail.com","sourabhkinra@gmail.com","tatti")
a.quit()
