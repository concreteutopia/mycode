#!/usr/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

eyes1=challenge[2][1]
goggles1=challenge[2][0]
nothing1=challenge[3]

print(f"My {eyes1}! The {goggles1} do {nothing1}!")

eyes2=goggles2=trial[2].get("goggles")
goggles2=trial[2].get("eyes")
nothing2=trial[3]
print(f"My {eyes2}! The {goggles2} do {nothing2}!")

eyes3=nightmare[0].get("user").get("name").get("first")
goggles3=nightmare[0].get("kumquat")
nothing3=nightmare[0].get("d")
print(f"My {eyes3}! The {goggles3} do {nothing3}!")

#alternate solutions
print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}!")
print(f"My {trial[2]['goggles']}! The {trial[2]['eyes']} do {trial[3]}!")
#alternate nightmare
eyes= nightmare[0]['user']['name']['first']
goggles= nightmare[0]['kumquat']
nothing= nightmare[0]['d']
print(f'My {nightmare[0]["user"]["name"]["first"]}! The {nightmare[0]["kumquat"]} do {nightmare[0]["d"]}!')
