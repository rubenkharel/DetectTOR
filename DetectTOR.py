import requests
import json
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
r = requests.get("https://dinace.me/detecttor/api/v1/",headers=headers)
soup = BeautifulSoup(r.content,'html.parser')
ver_soup = json.loads(soup.text)
length = len(ver_soup)
i = 0

def Status():
    print("1. LIVE\n"
          "2. DEAD\n"
          "3. Often Dead\n")
    userinp = int(input("Choose: "))
    if userinp == 1:
        y = "Live"
        print("Printing all the " + y + " sites.")
        for x in range(i, length):
            Live = ver_soup[x]["Status"]
            if Live.lower == y.lower:
                result = ver_soup[x]["Site"]

                print("Index " + str(x) + ".: " + result)
    elif userinp == 2:
        y = "Dead"
        print("Printing all the " + y + " sites.")
        for x in range(i, length):
            Live = ver_soup[x]["Status"]
            if Live.lower() == y.lower():
                result = ver_soup[x]["Site"]

                print("Index " + str(x) + ".: " + result)
    elif userinp == 3:
        y = "Often Dead"
        print("Printing all the " + y + " sites.")
        for x in range(i, length):
            Live = ver_soup[x]["Status"]
            if Live.lower() == y.lower():
                result = ver_soup[x]["Site"]

                print("Index " + str(x) + ".: " + result)
    else:
        print("invalid input, Closing...")
def Legit():
    print("1. TRUE\n"
          "2. UNVERIFIED\n"
          "3. FALSE\n")
    userinp = int(input("Choose: "))
    if userinp == 1:
        y = "TRUE"
        print("Printing all the " + y + " sites.")
        for x in range(i, length):
            Live = ver_soup[x]["Legit"]
            if Live.lower() == y.lower():
                result = ver_soup[x]["Site"]
                print("Index " + str(x) + ".: " + result)
    elif userinp == 2:
        y = "UNVERIFIED"
        print("Printing all the " + y + " sites.")
        for x in range(i, length):
            Live = ver_soup[x]["Legit"]
            if Live.lower() == y.lower():
                result = ver_soup[x]["Site"]

                print("Index " + str(x) + ".: " + result)
    elif userinp == 3:
        y = "False"
        print("Printing all the " + y + " sites.")
        for x in range(i, length):
            Live = ver_soup[x]["Legit"]
            if Live.lower() == y.lower():
                result = ver_soup[x]["Site"]

                print("Index " + str(x) + ".: " + result)
    else:
        print("invalid input, Closing...")

print("Filter site according to:\n"
      "1. Legit\n"
      "2. Status\n")
inp = int(input("Choose: "))
if inp == 1:
    Legit()
elif inp == 2:
    Status()
else:
    print("invalid input, Closing.")
