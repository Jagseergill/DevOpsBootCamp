from datetime import datetime

birthday_string = input("Enter your birthday (example - 20/09/2000):")
birthday_date = datetime.strptime(birthday_string, '%d/%m/%Y').date()
today = datetime.today()

difference_one = datetime(today.year, birthday_date.month, birthday_date.day)
difference_two = datetime(today.year+1, birthday_date.month, birthday_date.day)

days_till_birthday = 0
if difference_one > today:
    days_till_birthday = difference_one - today
else:
    days_till_birthday = difference_two - today

print(f"{days_till_birthday} days till your birthday.")
