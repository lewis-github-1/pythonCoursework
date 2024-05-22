from datetime import datetime, timedelta, date
# create a date object
tday = date.today()
print("Today is", tday)

#create a later date
bday = date(2023, 7, 6)
print("My birthday this year is", bday)

# find days between
# creates a timedelta (span)
days_until = bday - tday
print("Until my birthday: ", days_until)
print("days_until Object Type:", type(days_until))

# add 60 days using timedelta
new_date = tday + timedelta(days=60)
print("60 days from today: ", new_date)

# format dates using f-string
print("\nFormatting today's date using f-string:")
print(f"{tday:%c}")
print(f"{tday:%x}")
print(f"{tday:%a %b %d}")

#format dates using strftime() method of datetime class
print("\nFormatting today's date using strftime()")
print(tday.strftime("%c"))
print(tday.strftime("%x"))
print(tday.strftime("%a %b %d"))

# create a datetime object for now
dt_now = datetime.now()
print("Current - no time zone: ", dt_now) #UTC time
import pytz
dt_now_tz = dt_now.astimezone(pytz.timezone("US/Central"))
print("Current - Central time: ", dt_now_tz)

# create a datetime object manually
dt_halloween = datetime(2023, 10, 31)
print("Halloween: ", dt_halloween)
days_until_hall = dt_halloween - dt_now

#create a datetime from user input
str_birthdate = input("\nEnter your birthdate as mm/dd/yyyy: ")
dt_birthdate = datetime.strptime(str_birthdate, "%m/%d/%Y")
print(f"{dt_birthdate:%c}")


