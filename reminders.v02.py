import datetime

#usertime = int(input("what hour is it?" (0-23))

now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

if now.hour <= 5:
    print("Its early. You should be sleeping")
elif now.hour <=7:
    print("Wake up, brew that coffee, get that mile run in, and get that breakfast…")
elif now.hour <= 9:
    print("Time to go to work.")
elif now.hour <= 12:
    print("You should be working!")
elif now.hour <= 13:
    print("Take your lunch break!")
elif now.hour <= 17:
    print("Do you feel that afternoon?")
elif now.hour <= 19:
    print("Time to hit the gym...")
elif now.hour <= 21:
    print("GET THAT DINNER!")
elif now.hour <= 23:
    print("THEN GET THAT SLEEP!")
else:
    print("You didn't type an acceptable value! (0-23")