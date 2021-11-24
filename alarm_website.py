import time
import webbrowser

Set_Alarm = input("Set the website alarm as H:M:S(all in two digits): ")
url = input("Enter the website you want to open: ")
Actual_Time = time.strftime("%I:%M:%S")

while (Actual_Time != Set_Alarm):
    print("The time is " + Actual_Time)
    Actual_Time = time.strftime("%I:%M:%S")
    time.sleep(1)
if(Actual_Time == Set_Alarm):
    print("You should see you webpage now :)")
    webbrowser.open(url)