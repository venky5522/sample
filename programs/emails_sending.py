import smtplib

email = input("LOGIN...\n Email - ")
password = input("Password- ")
receiver_email = input("Receiver's Email- ")
message = input("Type Your message- ")

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email,password)
print("Logged in Successfully!!!!")
print("Email is Sending....")
server.sendmail(email,receiver_email,message)
server.quit()
print("Email is sent....")