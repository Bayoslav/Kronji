import requests

##
def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login('zeaitirsamer5@gmail.com', 'Samerz2010')
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        try:
            print("failed to send mail, sending through another account")
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            print('successfully sent the mail')
        except:
            send_simple_message(message)


##message = "Price: " + price + "\nTitle: " + title + "\nCity: " + link + "\nLink: " + carurl
# send_email('zeaitirsamer5@gmail.com','Samerz2010','Bzeaiter@gmail.com','PyCrawler IL',message)
#send_email('zeaitirsamer5@gmail.com','Samerz2010',['Bzeaiter@gmail.com','6308128805@tmomail.net'],'PyCrawler IL',message)
cars = ''
for car in range(0,5,1):
    name = "Car: " + str(car) + '\n'
    price = 'Price: ' + str(car+100) + '\n'
    city = 'Link: https' + str(car) + '.com\n'
    cars = cars + name + price + city 

send_email('zeaitirsamer5@gmail.com','Samerz2010',['Bzeaiter@gmail.com','6308128805@tmomail.net'],'PyCrawler TEST',cars)

#send_email('zeaitirsamer5@gmail.com')
