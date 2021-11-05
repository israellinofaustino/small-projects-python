# Import Libraries
import time
from datetime import datetime as dt
#Windows host file path
host_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
#Add the website you want to block, in this list
#Example: you need add this line in hosts file "127.0.0.1 www.github.com *\n* 127.0.0.1 github.com"
website_list = ["www.github.com/", "github.com"]
while True:
    #Duration during which, website blocker will work. (from 9am to 24pm)
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,00):
        print("Sorry not allowed...")

        with open(host_path,'r+') as file:
            contend = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
        print("All the listed websites are blocked")
        break
    else:
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                    file.truncate()
                print("Allowed access!")
            break