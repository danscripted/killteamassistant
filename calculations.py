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
     print(f"{operative['name']}")
     print(f"{'MOV' :<6} {'APL' :<6} {'DEF' :<6} {'SAVE' :<6} {'WOUNDS' :<6}")
     print(f"{operative['movement']:<6} {operative['apl']:<6} {operative['defence']:<6} {operative['save']:<6} {operative['wounds']:<6}")
     print(f"WEAPONS")
     for weapon_name, weapon in operative["weapons"].items():
        print(weapon_name)
        print(f"{'  ATK:':>4}{weapon['attacks']} {'BS:':<4}{weapon['bs']} {'DAM:':<4}{weapon['normal_damage']}")
        print(f"  Rules: {', '.join(weapon['special_rules'])}")
        
     
    
     

# print(f"Name: {operative['name']} \nMOV: \n{operative['movement']}")
#      print(f"================================================")
#      print(f"Actions APL: {operative['apl']}")
#      print(f"Defence: {operative['defence']}")
#      print(f"Save: {operative['save']}")
#      print(f"Wounds: {operative['wounds']}")


display_operative(operatives["Assault Intercessor Sergeant"])
