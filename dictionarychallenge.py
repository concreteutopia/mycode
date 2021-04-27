#!/usr/bin/env python3

#https://github.com/csfeeser/Python/blob/master/challenges/DICTIONARIES-%20tuesday.md

heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "magic",
    "archenemy": "Voldemort",},
"captain america":
    {"real name": "Steve Rogers",
    "powers": "frisbee shield",
    "archenemy": "Hydra",}
        }

char_name=input("Which character do you want to know about? (Wolverine, Harry Potter, Captain America): ")
char_stat=input("What statistic do you want to know about? (real name, powers, archenemy): ")

answer=heroes[char_name.lower()].get(char_stat,"not found")

print(f"{char_name.title()}'s {char_stat} is: {answer}")
