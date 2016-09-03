import smtplib

def send_emails(emails, schedule, forecast):
    try:
        gmail_file = open('gmail_api.txt', 'r')

        gmail_api = gmail_file.read()
    except FileNotFoundError as err:
        print(err)
    # Connecting to the server (gmail)
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encrypton
    server.starttls()

    # Password Input
    # password = input("What's your password?")
    password = gmail_api
    # Login
    server.login('pope410211@gmail.com', password)

    # Send to entire mail list
    for to_email, name in emails.items():
        message = "Subject: Today's Events!\n"
        message += "Hello " + name + '!\n\n'
        message += forecast + '\n\n'
        message += schedule + '\n\n'
        message += "Let's have a great day!"
        server.sendmail('pope410211@gmail.com', to_email, message)

    server.quit()
