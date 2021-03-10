import smtplib, ssl

def sendEmail(message, sender="cat.cs.development@gmail.com", receiver="catrondini@gmail.com"):
    port = 465 #SSL Connection
    password = input("Please enter password: ")
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL("smtp.gmail.com", port=port, context=context) as server:
        server.login("cat.cs.development@gmail.com", password)
        server.sendmail(sender, receiver, message)
    
    return