import json
import random
import secrets

data = json.load(open("operatives.json", encoding="utf-8"))
team_name = list(data.keys())[0]
# Get the operatives sub-dictionary
operatives = data[team_name]["operatives"]

def operative_menu():
    print(f"Angels of Death - Kill Team Assistant")
    print(f"======================================")
    
    for index, name in enumerate(operatives, start=1):
        print(f"{index}. {name}")
    selection = input("Select an operative:")
    operatives_list = list(operatives.keys())
    chosen = operatives_list[int(selection) - 1]

    print(f"You have selected {chosen}")
    

    for index, name in enumerate(operatives[chosen]["weapons"], start=1):
        print(f"{index}. {operatives[chosen]["weapons"]}")
    weapons_list = list
    selection_weapon = input("Select a weapon:")

operative_menu()

def display_operative(operative):
     print(f"{operative['name']}")
     print(f"{'MOV' :<6} {'APL' :<6} {'DEF' :<6} {'SAVE' :<6} {'WOUNDS' :<6}")
     print(f"{operative['movement']:<6} {operative['apl']:<6} {operative['defence']:<6} {operative['save']:<6} {operative['wounds']:<6}")
     print(f"WEAPONS")
     for weapon_name, weapon in operative["weapons"].items():
        print(weapon_name)
        print(f"{'  ATK:':>4}{weapon['attacks']} {'BS:':<4}{weapon['bs']} {'DAM:':<4}{weapon['normal_damage']}")
        print(f"  Rules: {', '.join(weapon['special_rules'])}")
        
display_operative(operatives["Assault Intercessor Sergeant"])     
    
# def simulate_attack(weapon):
#     print(f"Rolling attack:")
#     print("=========================")
#     normal_hits = 0
#     crit_hits = 0
#     for i in range(weapon['attacks']):
#        roll = random.randint(1, 6)
#        if roll == 6:
#         crit_hits += 1
#        elif roll >= weapon['bs']:
#             normal_hits += 1
#     print(f"Normal hits: {normal_hits} Crit hits: {crit_hits}")
#     total_damage = (normal_hits * weapon['normal_damage'] + (crit_hits * weapon['crit_damage']))
#     print (f"{total_damage}")    

# simulate_attack(operatives["Assault Intercessor Sergeant"]["weapons"]["Hand Flamer"])



def simulate_attack(weapon):
    print(f"Rolling attack:")
    print("=========================")
    # setup
    total_damage_simmed = 0
    simulations = 1000
    # dice rolls
    for sim in range (simulations):
        normal_hits = 0
        crit_hits = 0
        for i in range(weapon['attacks']):
            roll = random.randint(1, 6)
            if roll == 6:
                crit_hits += 1
            elif roll >= weapon['bs']:
                normal_hits += 1
        # Calculations
        total_damage = (normal_hits * weapon['normal_damage'] + (crit_hits * weapon['crit_damage']))
        total_damage_simmed += total_damage   
    
    average_damage = total_damage_simmed / simulations
    print(f"Average damage over {simulations} simulations: {average_damage:.2f}")    

simulate_attack(operatives["Assault Intercessor Sergeant"]["weapons"]["Hand Flamer"])