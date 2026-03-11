import json
import random

import json
data = json.load(open("operatives.json", encoding="utf-8"))


team_name = list(data.keys())[0]

display_name = team_name.title()

# Get the operatives sub-dictionary
operatives = data[team_name]["operatives"]

print(f"Team: {display_name}")
print(f"Number of operatives: {len(operatives)}")
print("Operative names:", list(operatives.keys()))
