import weather
import send_gmail

def get_emails():
    emails = {}

    try:
        email_list = open('emailList.txt', 'r')

        for line in email_list:
            (email, name) = line.split(',')
            emails[email] = name.strip()

    except FileNotFoundError as err:
        print(err)

    return emails

def get_schedule():
    try:
        schedule_list = open('schedule.txt', 'r')

        schedule = schedule_list.read()
    except FileNotFoundError as err:
        print(err)

    return schedule

def main():
    emails = get_emails()
    schedule = get_schedule()
    forecast = weather.get_weather()
    send_gmail.send_emails(emails, schedule, forecast)
    # print(emails, schedule, forecast)

main()
