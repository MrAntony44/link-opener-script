import json
import datetime
import webbrowser
import time
import pyperclip
from win10toast import ToastNotifier

toast = ToastNotifier()


dateFormat = datetime.datetime.now()
day = dateFormat.strftime("%A")
hour = dateFormat.strftime("%H")
minute = dateFormat.strftime("%M")
hourStr = str(hour)
minuteStr = str(minute)
timeRawStr = hourStr + minuteStr
timeInt = int(timeRawStr)
timeRaw = str(timeInt)

if timeRaw >= "940":
    timeRaw = "1000"

with open('config.json') as json_file:
    data = json.load(json_file)
    program = data['program']
    links = data['links']
    timetable = data['timetable']

    if timeRaw >= timetable["1"]["startTime"] and timeRaw <= timetable["1"]["endTime"]:
        lesson = program[day]["1"]
        link = links[lesson]
        print("Your lesson right now is:", lesson.upper())
        print(link)
        webbrowser.open(link, new=0, autoraise=False)
        pyperclip.copy(link)
        toastMessage = day.upper() + "\n1st hour(8:00-8:40) " + lesson + " (NOW)\n2nd hour(8:50-9:30) " + program[day]["2"] + "\n3rd hour(9:40-10:20) " + program[day]["3"] + "\n4th hour(10:30-11:10) " + program[day]["4"] + "\n5th hour(11:20-12:00) " + program[day]["5"] + "\n6th hour(12:10-12:50) " + program[day]["6"] + "\n7th hour(13:00-13:40) " + program[day]["7"]
        f = open("day_program.txt", "w")
        f.write(toastMessage)
        f.close()
        webbrowser.open('program.html', new=0, autoraise=True)
        toast.show_toast("Lesson Notification","Just joined " + lesson + " class.\n\nNext up: " + program[day]["2"],duration=10)
        time.sleep(2)
    elif timeRaw >= timetable["2"]["startTime"] and timeRaw <= timetable["2"]["endTime"]:
        lesson = program[day]["2"]
        link = links[lesson]
        print("Your lesson right now is:", lesson.upper())
        print(link)
        webbrowser.open(link, new=0, autoraise=False)
        pyperclip.copy(link)
        toast.show_toast("Lesson Notification","Just joined " + lesson + " class.\n\nNext up: " + program[day]["3"],duration=10)
        time.sleep(2)
    elif timeRaw >= timetable["3"]["startTime"] and timeRaw <= timetable["3"]["endTime"]:
        lesson = program[day]["3"]
        link = links[lesson]
        print("Your lesson right now is:", lesson.upper())
        print(link)
        webbrowser.open(link, new=0, autoraise=False)
        pyperclip.copy(link)
        toast.show_toast("Lesson Notification","Just joined " + lesson + " class.\n\nNext up: " + program[day]["4"],duration=10)
        time.sleep(2)
    elif timeRaw >= timetable["4"]["startTime"] and timeRaw <= timetable["4"]["endTime"]:
        lesson = program[day]["4"]
        link = links[lesson]
        print("Your lesson right now is:", lesson.upper())
        print(link)
        webbrowser.open(link, new=0, autoraise=False)
        pyperclip.copy(link)
        toast.show_toast("Lesson Notification","Just joined " + lesson + " class.\n\nNext up: " + program[day]["5"],duration=10)
        time.sleep(2)
    elif timeRaw >= timetable["5"]["startTime"] and timeRaw <= timetable["5"]["endTime"]:
        lesson = program[day]["5"]
        link = links[lesson]
        print("Your lesson right now is:", lesson.upper())
        print(link)
        webbrowser.open(link, new=0, autoraise=False)
        pyperclip.copy(link)
        toast.show_toast("Lesson Notification","Just joined " + lesson + " class.\n\nNext up: " + program[day]["6"],duration=10)
        time.sleep(2)
    elif timeRaw >= timetable["6"]["startTime"] and timeRaw <= timetable["6"]["endTime"]:
        lesson = program[day]["6"]
        link = links[lesson]
        print("Your lesson right now is:", lesson.upper())
        print(link)
        webbrowser.open(link, new=0, autoraise=False)
        pyperclip.copy(link)
        toast.show_toast("Lesson Notification","Just joined " + lesson + " class.\n\nNext up: " + program[day]["7"],duration=10)
        time.sleep(2)
    elif timeRaw >= timetable["7"]["startTime"] and timeRaw <= timetable["7"]["endTime"]:
        lesson = program[day]["7"]
        link = links[lesson]
        print("Your lesson right now is:", lesson.upper())
        print(link)
        webbrowser.open(link, new=0, autoraise=False)
        pyperclip.copy(link)
        toast.show_toast("Lesson Notification","Just joined " + lesson + " class.\n\nLast class of the day!",duration=10)
        time.sleep(2)
    else:
        print("Hey, you dont have a lesson right now!!")
        toast.show_toast("No lesson right now!","You dont have any lesson right now!",duration=10)
        time.sleep(2)
