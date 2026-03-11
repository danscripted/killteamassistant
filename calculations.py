import json
import random

data = json.load(open("operatives.json", encoding="utf-8"))


team_name = list(data.keys())[0]

display_name = team_name.title()

# Get the operatives sub-dictionary
operatives = data[team_name]["operatives"]

# print(f"Team: {display_name}")
# print(f"Number of operatives: {len(operatives)}")
# print("Operative names:", list(operatives.keys()))

# print(data["angels of death"]["operatives"]["Intercessor Warrior"]["movement"])

def display_operative(operative):
     print(f"Name: {operative["name"]}")
     print(f"Movement: {operative["movement"]}")
     print(f"Actions APL: {operative["apl"]}")
     print(f"Defence: {operative["defence"]}")
     print(f"Save: {operative["save"]}")
     print(f"Wounds: {operative["wounds"]}")


display_operative(data["angels of death"]["operatives"]["Intercessor Warrior"])