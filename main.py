import twitch
import os
import webbrowser
from googletrans import Translator
import re


# Global Vars
translator = Translator()
language = re.findall(r"[\w']+", open('./settings.ini').read())[1]
clientId = os.environ["TWITCH_CLIENT_ID"]
clientSecret = ""
code = "vide"


# pyinstaller <filename.py> ---> filename.exe


if __name__ == '__main__':

    print("###############################################################")
    print("############################MY TWICTH BOT######################")
    print("######################################@Author: Blingbike :)####")

    if not os.path.exists("./settings.ini"):
        print("Choose the language FR(1) | EN(2) :", end="")
        language = input()

        print(translator.translate(f"Your language setting : {language}", dest=language).text)

        if re.findall(r"[\w']+", open('./settings.ini').read())[3] != "SET":
            print(translator.translate("Your client Id:", dest=language).text, end="")
            clientId = input()
            print(translator.translate("Your client secret:", dest=language).text, end="")
            clientSecret = input()

    try:
        os.environ["TWITCH_CLIENT_ID"]
    except KeyError:
        os.environ["TWITCH_CLIENT_ID"] = clientId

    try:
        os.environ["TWITCH_SECRET"]
    except KeyError:
        os.environ["TWITCH_SECRET"] = clientSecret

    with open("./settings.ini", "w") as file:
        file.write(f"LANGUAGE={language}\n")
        file.write(f"ENV=SET\n")
        file.close()

if twitch.connect().__contains__("failed"):
    print(translator.translate("Confirm by pressing enter to authenticate on the web browser...", dest=language).text,
          end="")
    input()
    webbrowser.open("https://twitchapps.com/tmi/")
    print(translator.translate("Paste the generated password:", dest=language).text, end="")
    os.environ["TWITCH_OAUTH_TOKEN"] = input()
    twitch.connect()

print("logged")
