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
        
display_operative(operatives["Assault Intercessor Warrior"])     
    
def simulate_attack(weapon):
    normal_hits = 0
    crit_hits = 0
    for i in range(weapon['attacks']):
       roll = random.randint(1, 6)
       if roll == 6:
        crit_hits += 1
       elif roll >= weapon['bs']:
            normal_hits += 1
    print(f"Normal hits: {normal_hits} Crit hits: {crit_hits}")
    total_damage = (normal_hits * weapon['normal_damage'] + (crit_hits * weapon['crit_damage']))
    print (f"{total_damage}")    

simulate_attack(operatives["Assault Intercessor Warrior"]["weapons"]["Heavy Bolt Pistol"])

