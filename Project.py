from time import sleep
from getpass import getpass
from instabot import Bot
from os import remove

my_bot = Bot()

print("WELCOME TO INSTABOT APPLICATION")
sleep(2)
print("--setting up the connection with https://www.instagaram.com/", end="")
for i in range(3):
    sleep(3)
    print('.', end="")

print()

sleep(2)
print("Connection Established!")

# login setup
username = input("username: ")
password = getpass(prompt="password: ")
my_bot.login(username=username, password=password)
print("f--{username} Log in Successfull!! ")

while True:
    print("Chooose Suitable Options: ")
    print("""1.Follow User\n2. Unfollow User\n3. Send Message to User\n4.Exit the App""")
    print("Enter Option of Your Choice: ", end="")

    n - int(input())
    if n==1:
        user = input("Enter Username: ")
        my_bot.Follow(user)
        print(F"--{user} FOLLOWED.--")
    elif n==2:
        user = input("Enter Username: ")
        my_bot.Unfollow(user)
        print(F"--{user} UNFOLLOWED.--")
    elif n==3:
        user = input("Enter Username: ")
        message = input("Enter message you want to send: ")
        my_bot.send_message(message, user)
        print(F"--MESSAGE SUCCESSFULLY SEND TO{user}.--")
    elif n==4:
        my_bot.logout()
        print("Logging out the user", end="")

        for i in range(3):
            sleep(1)
            print('.', end="")

            print()

            sleep(2)
            print("Connection Ended!")
            print("Logged out Successfully!")
            break
    else:
        print("--WRONG INPUT, choose AGAIN")

remove('./config')