#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests, random

def main():
    factlist=[]
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')
    
    #status_code', 'text', 'url'
    print(f"Status code: {r.status_code}")
    print(f"URL: {r.url}")

    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
    ## print the value associated with text"
    for catfact in r.json():
        #print(catfact.get("text"))  # the .get() method returns NONE if key not found
        factlist.append(catfact.get("text"))

    #print(factlist)
    print(random.choice(factlist))

main()

