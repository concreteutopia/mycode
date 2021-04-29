#!/usr/bin/env python3

#List out all of Muhammad Ali's favorite foods
#Write a email body that contains Ali's phone and email
#Return the cost of Ali's favorite meal
#Advertise Ali's soda! Say Muhammad Ali's favorite drink once for every single win he's ever had!

ali={"name":{"birth":"Cassius Clay","current":"Muhammad Ali"},"contact":{"phone":"333-444-5555","email":"thebest@boxing.com"},"favorites":{"number":56,"food":{"baked chicken":3.5,"mac and cheese":4.5,"spinach":2,"green peas":2},"drink":{"adult":["none"],"nonadult":["Mr. Champ soda"]}}}

favefoods=(ali['favorites'].get('food').keys())
mealcost = 0.0

print("Ali's favorite foods: ")

for food in favefoods:
    print(food)
    foodcost=ali['favorites'].get('food')[food]
    mealcost += float(foodcost)

print(f"The cost of Ali's favorite meal: {mealcost}")

print("Email contents")
print(f"Phone: {ali['contact']['phone']}")
print(f"Email: {ali['contact']['email']}")

print(f"Ali wins: {ali['favorites'].get('number')}")

favedrink=ali['favorites']['drink']['nonadult']
#doesn't work below
for x in ali['favorites'].get('number'):
    print(f"{favedrink}")

