#!/usr/bin/env python3
#https://github.com/csfeeser/Python/blob/master/challenges/FOR%20LOOP%20DICTIONARY-%20farm_dictionary.md

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


def function1():
    for animal in farms[0]['agriculture']:
        print(animal)


def function2():
    farmlist = []
    for farm in farms:
        farmlist.append(farm['name'])
    pickfarm=input(f"Please choose a farm {farmlist} to see the agriculture that is raised there: ")
    print(f"The agriculture raised at {pickfarm} is:")
    for agri in farms[farmlist.index(pickfarm)]['agriculture']:
        print(agri)


def function3():
    animalslist=["sheep", "cows", "pigs", "chickens", "llamas", "cats"]

    farmlist = []
    for farm in farms:
        farmlist.append(farm['name'])
    pickfarm=input(f"Please choose a farm {farmlist} to ONLY see the animals that are raised there: ")

    print(f"The ANIMALS  raised at {pickfarm} are:")
    for agri in farms[farmlist.index(pickfarm)]['agriculture']:
        if agri in animalslist:
            print(agri)
                

function1()
function2()
function3()

    
