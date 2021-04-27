#!/usr/bin/env python3

import datetime


weirdholidays= {
"january":
	{"jan 1": "Polar Bear Plunge Day",
	"jan 2": "Buffet Day",
	"jan 2": "Run It up the Flagpole and See If Anyone Salutes It Day",
	"jan 2": "Science Fiction Day",
	"jan 3": "Fruitcake Toss Day",
	"jan 3": "Festival of Sleep Day",
	"jan 4": "Trivia Day",
	"jan 5": "Bird Day",
	"jan 6": "Bean Day",
	"jan 7": "Old Rock Day",
	"jan 8": "Earth's Rotation Day",
	"jan 9": "Static Electricity Day",
	"jan 9": "Word Nerd Day",
	"jan 10": "Cut Your Energy Costs Day",
	"jan 11": "Learn Your Name in Morse Code Day",
	"jan 11": "Clean Off Your Desk Day",
	"jan 12": "marzipan Day",
	"jan 13": "Make Your Dreams Come True Day",
	"jan 14": "Organize Your Home Day",
	"jan 15": "Strawberry Ice Cream Day",
	"jan 15": "Bagel and Lox Day",
	"jan 16": "Nothing Day",
	"jan 16": "Soup Swap Day",
	"jan 17": "Benjamin Franklin Day",
	"jan 17": "Kid Inventors' Day",
	"jan 17": "Ditch New Year's Resolution Day",
	"jan 18": "Thesaurus Day",
	"jan 19": "Tin Can Day",
	"jan 19": "Popcorn Day",
	"jan 20": "Penguin Awareness Day",
	"jan 21": "Squirrel Appreciation Day",
	"jan 22": "Hot Sauce Day",
	"jan 22": "Answer Your Cat's Questions Day",
	"jan 23": "Handwriting Day",
	"jan 24": "Compliment Day",
	"jan 24": "Macintosh Computer Day",
	"jan 25": "Opposite Day",
	"jan 26": "Spouse's Day",
	"jan 27": "Chocolate Cake Day",
	"jan 27": "e-Day",
	"jan 28": "Data Privacy Day",
	"jan 28": "Fun at Work Day",
	"jan 29": "Puzzle Day",
	"jan 30": "Croissant Day",
	"jan 31": "Backwards Day",},
"february":

	{"feb 2": "Day of the Crêpe",
	"feb 2": "Play Your Ukulele Day",
	"feb 3": "Carrot Cake Day",
	"feb 4": "Thank Your Mailman Day",
	"feb 4": "Create a Vacuum Day",
	"feb 4": "Stuffed Mushroom Day",
	"feb 5": "Work Naked Day",
	"feb 5": "National Weatherperson's Day",
	"feb 5": "Chocolate Fondue Day",
	"feb 6": "Eat Ice Cream for Breakfast Day",
	"feb 6": "Lame Duck Day",
	"feb 7": "e-Day",
	"feb 7": "Send a Card to a Friend Day",
	"feb 8": "Laugh and Get Rich Day",
	"feb 8": "Clean Out Your Computer Day",
	"feb 9": "Toothache Day",
	"feb 9": "Bagel and Lox Day",
	"feb 10": "Umbrella Day",
	"feb 11": "Make a Friend Day",
	"feb 11": "Don't Cry Over Spilled Milk Day",
	"feb 12": "Darwin Day",
	"feb 13": "World Radio Day",
	"feb 14": "Ferris Wheel Day",
	"feb 14": "Library Lovers Day",
	"feb 15": "Gumdrop Day",
	"feb 16": "Do a Grouch a Favor Day",
	"feb 17": "Random Act of Kindness Day",
	"feb 18": "Battery Day",
	"feb 19": "Chocolate Mint Day",
	"feb 22": "Single Tasking Day",
	"feb 22": "Be Humble Day",
	"feb 23": "International Dog Biscuit Appreciation Day",
	"feb 24": "Tortilla Chip Day",
	"feb 26": "Pistachio Day",
	"feb 26": "Tell a Fairy Tale Day",
	"feb 27": "International Polar Bear Day",
	"feb 27": "No Brainer Day",
	"feb 27": "World Sword Swallowers Day",
	"feb 28": "Public Sleeping Day",},
"march":
	{"mar 1": "World Compliment Day",
	"mar 1": "Plan a Solo Vacation Day",
	"mar 2": "Old Stuff Day",
	"mar 3": "I Want You to be Happy Day",
	"mar 4": "march Forth and Do Something Day",
	"mar 5": "Learn What Your Name Means Day",
	"mar 5": "Cinco de marcho",
	"mar 6": "Dentist’s Day",
	"mar 7": "Alexander Graham Bell Day",
	"mar 8": "Proofreading Day",
	"mar 10": "mario Day",
	"mar 11": "Oatmeal Nut Waffle Day",
	"mar 12": "Alfred Hitchcock Day",
	"mar 13": "Jewel Day",
	"mar 14": "Pi Day",
	"mar 15": "Napping Day",
	"mar 15": "Everything You Think is Wrong Day",
	"mar 16": "Every Thing You Do is Right Day",
	"mar 17": "Submarine Day",
	"mar 18": "Absolutely Incredible Kid Day",
	"mar 18": "Awkward Moments Day",
	"mar 19": "Let's Laugh Day",
	"mar 20": "World Storytelling Day",
	"mar 20": "Proposal Day",
	"mar 21": "Common Courtesy Day",
	"mar 22": "International Goof Off Day",
	"mar 23": "Puppy Day",
	"mar 23": "Near Miss Day",
	"mar 24": "Chocolate Covered Raisins Day",
	"mar 25": "Waffle Day",
	"mar 25": "Tolkien Reading Day",
	"mar 26": "Make Up Your Own Holiday Day",
	"mar 27": "Spanish Paella Day",
	"mar 28": "Something on a Stick Day",
	"mar 29": "Smoke and Mirrors Day",
	"mar 30": "Take a Walk in the Park Day",
	"mar 31": "Bunsen Burner Day",},
"april":	
	{"apr 1": "Fun at Work Day",
	"apr 2": "Walk to Work Day",
	"apr 3": "World Party Day",
	"apr 4": "Tell a Lie Day",
	"apr 5": "Read a Road Map Day",
	"apr 5": "First Contact Day",
	"apr 6": "Sorry Charlie Day",
	"apr 10": "Siblings Day",
	"apr 11": "Submarine Day",
	"apr 11": "Barbershop Quartet Day",
	"apr 12": "Grilled Cheese Day",
	"apr 12": "Yuri's Night",
	"apr 13": "Be Kind to Lawyers Day",
	"apr 13": "Scrabble Day",
	"apr 14": "International Moment of Laughter Day",
	"apr 14": "Reach as High as You Can Day",
	"apr 14": "Look up the Sky Day",
	"apr 16": "Eggs Benedict Day",
	"apr 16": "Wear Pajamas to Work Day",
	"apr 17": "Haiku Poetry Day",
	"apr 18": "Columnist Day",
	"apr 20": "Look Alike Day",
	"apr 22": "Jelly Bean Day",
	"apr 22": "Take Our Daughters and Sons to Work Day",
	"apr 23": "Take a Chance Day",
	"apr 23": "Impossible Astronaut Day",
	"apr 23": "Lover's Day",
	"apr 25": "DNA Day",
	"apr 25": "World Pinhole Photography Day",
	"apr 26": "Pretzel Day",
	"apr 26": "Richter Scale Day",
	"apr 29": "Zipper Day",
	"apr 30": "Honesty Day",},
"may":	
	{"may 1": "Batman Day",
	"may 1": "Herb Day",
	"may 1": "Free Comic Book Day",
	"may 4": "Star Wars Day",
	"may 6": "Beverage Day",
	"may 7": "No Pants Day",
	"may 7": "Space Day",
	"may 9": "Europe Day",
	"may 9": "Lost Sock Memorial Day",
	"may 10": "Clean Up Your Room Day",
	"may 11": "Twilight Zone Day",
	"may 11": "Eat What You Want Day",
	"may 12": "National School Nurse Day",
	"may 12": "Limerick Day",
	"may 13": "Frog Jumping Day",
	"may 14": "Dance Like a Chicken Day",
	"may 15": "Chocolate Chip Day",
	"may 17": "Pack Rat Day",
	"may 18": "No Dirty Dishes Day",
	"may 19": "may Ray Day",
	"may 20": "Be a Millionaire Day",
	"may 21": "Pizza Party Day",
	"may 21": "Talk Like Yoda Day",
	"may 22": "Buy a Musical Instrument Day",
	"may 24": "Scavenger Hunt Day",
	"may 25": "Sing Out Day",
	"may 25": "Towel Day",
	"may 26": "World Lindy Hop Day",
	"may 27": "Sun Screen Day",
	"may 28": "Hamburger Day",
	"may 29": "Put a Pillow on Your Fridge Day",
	"may 30": "My Bucket's Got a Hole Day",
	"may 31": "Macaroon Day",},
"june":	
	{"jun 1": "Say Something Nice Day",
	"jun 2": "Leave the Office Early Day",
	"jun 3": "Repeat Day",
	"jun 4": "Hug Your Cat Day",
	"jun 4": "National Doughnut Day",
	"jun 6": "Drive-In Movie Day",
	"jun 7": "VCR Day",
	"jun 8": "Best Friends Day",
	"jun 9": "Donald Duck Day",
	"jun 10": "Iced Tea Day",
	"jun 11": "Corn on the Cob Day",
	"jun 12": "Red Rose Day",
	"jun 13": "Sewing Machine Day",
	"jun 14": "Bourbon Day",
	"jun 15": "Nature Photography Day",
	"jun 16": "Bloomsday",
	"jun 17": "Eat Your Vegetables Day",
	"jun 18": "International Picnic Day",
	"jun 18": "International Panic Day",
	"jun 19": "World Juggling Day",
	"jun 19": "Sauntering Day",
	"jun 21": "Daylight Appreciation Day",
	"jun 22": "Onion Ring Day",
	"jun 23": "Typewriter Day",
	"jun 24": "Swim a Lap Day",
	"jun 25": "Take Your Dog to Work Day",
	"jun 25": "Please Take my Children to Work Day",
	"jun 26": "Chocolate Pudding Day",
	"jun 27": "Helen Keller Day",
	"jun 28": "Tau Day",
	"jun 29": "Camera Day",
	"jun 30": "Meteor Watch Day",},
"july":	
	{"jul 1": "International Joke Day",
	"jul 2": "I Forgot Day",
	"jul 2": "World UFO Day",
	"jul 3": "Compliment Your Mirror Day",
	"jul 3": "International Plastic Bag Free Day",
	"jul 4": "Sidewalk Egg Frying Day",
	"jul 5": "Workaholics Day",
	"jul 6": "World Kissing Day",
	"jul 7": "Tell the Truth Day",
	"jul 8": "Video Games Day",
	"jul 8": "Math 2.0 Day",
	"jul 9": "Sugar Cookie Day",
	"jul 10": "Teddy Bears' Picnic Day",
	"jul 10": "Clerihew Day",
	"jul 11": "Cheer Up the Lonely Day",
	"jul 12": "Simplicity Day",
	"jul 13": "Embrace Your Geekness Day",
	"jul 14": "Pandemonium Day",
	"jul 15": "Gummi Worm Day",
	"jul 16": "Corn Fritters Day",
	"jul 17": "Yellow Pig Day",
	"jul 17": "World Emoji Day",
	"jul 18": "Insurance Nerd Day",
	"jul 18": "Caviar Day",
	"jul 18": "Ice Cream Day",
	"jul 19": "Stick Out Your Tongue Day",
	"jul 20": "Space Exploration Day",
	"jul 21": "junk Food Day",
	"jul 22": "Pi Approximation Day",
	"jul 23": "Vanilla Ice Cream Day",
	"jul 24": "Cousins Day",
	"jul 25": "Culinarians Day",
	"jul 26": "Uncle and Aunt Day",
	"jul 27": "Take your Pants for a Walk Day",
	"jul 28": "Milk Chocolate Day",
	"jul 29": "Lasagna Day",
	"jul 30": "National Cheesecake Day",
	"jul 31": "Uncommon Musical Instrument Day",},
"august":	
	{"aug 1": "National Girlfriend Day",
	"aug 1": "Sisters' Day",
	"aug 2": "Ice Cream Sandwich Day",
	"aug 3": "Watermelon Day",
	"aug 4": "Single Working Women's Day",
	"aug 5": "Work Like a Dog Day",
	"aug 6": "Fresh Breath Day",
	"aug 6": "International Beer Day",
	"aug 7": "Lighthouse Day",
	"aug 8": "Happiness Happens Day",
	"aug 9": "Book Lovers Day",
	"aug 10": "Lazy Day",
	"aug 11": "Son and Daughter Day",
	"aug 12": "Middle Child Day",
	"aug 13": "Left-Handers Day",
	"aug 14": "Creamsicle Day",
	"aug 15": "Relaxation Day",
	"aug 16": "Tell a Joke Day",
	"aug 17": "Thrift Shop Day",
	"aug 18": "Mail Order Catalog Day",
	"aug 19": "World Photo Day",
	"aug 20": "Chocolate Pecan Pie Day",
	"aug 21": "Spumoni Day",
	"aug 22": "Be An Angel Day",
	"aug 23": "Ride Like the Wind Day",
	"aug 24": "Pluto Demoted Day",
	"aug 25": "Kiss and Make up Day",
	"aug 26": "Dog Appreciation Day",
	"aug 27": "The Duchess Who Wasn't Day",
	"aug 28": "Bow Tie Day",
	"aug 29": "According to Hoyle Day",
	"aug 30": "Frankenstein Day",
	"aug 31": "Eat Outside Day",},
"september":	
	{"sep 1": "Emma Nutt Day",
	"sep 1": "No Rhyme or Reason Day",
	"sep 2": "Bison Ten Yell Day",
	"sep 3": "Skyscraper Day",
	"sep 4": "Eat an Extra Dessert Day",
	"sep 5": "Be Late for Something Day",
	"sep 5": "Cheese Pizza Day",
	"sep 6": "Fight Procrastination Day",
	"sep 6": "Read a Book Day",
	"sep 7": "Salami Day",
	"sep 8": "Pardon Day",
	"sep 9": "Teddy Bear Day",
	"sep 10": "Swap Ideas Day",
	"sep 11": "Make Your Bed Day",
	"sep 12": "Chocolate Milkshake Day",
	"sep 13": "Positive Thinking Day",
	"sep 13": "Roald Dahl Day",
	"sep 14": "Hug Your Hound Day",
	"sep 15": "Make a Hat Day",
	"sep 16": "Collect Rocks Day",
	"sep 16": "Guacamole Day",
	"sep 17": "International Country Music Day",
	"sep 18": "National CleanUp Day",
	"sep 18": "Rice Krispie Treat Day",
	"sep 19": "National Gymnastics Day",
	"sep 19": "International Talk Like a Pirate Day",
	"sep 20": "Punch Day",
	"sep 21": "Miniature Golf Day",
	"sep 22": "Hobbit Day",
	"sep 23": "Checkers Day",
	"sep 24": "Punctuation Day",
	"sep 25": "Comic Book Day",
	"sep 26": "Love Note Day",
	"sep 27": "Crush a Can Day",
	"sep 28": "Ask a Stupid Question Day",
	"sep 28": "Good Neighbor Day",
	"sep 30": "Hot Mulled Cider Day",},
"october":	
	{"oct 1": "International Coffee Day",
	"oct 1": "Balloons Around the World Day",
	"oct 1": "World Smile Day",
	"oct 2": "Card Making Day",
	"oct 2": "Phileas Fogg Wager Day",
	"oct 4": "Taco Day",
	"oct 5": "Chic Spy Day",
	"oct 6": "Mad Hatter Day",
	"oct 7": "Frappé Day",
	"oct 8": "Pierogi Day",
	"oct 9": "Curious Events Day",
	"oct 10": "Handbag Day",
	"oct 11": "It's My Party Day",
	"oct 12": "Old Farmers Day",
	"oct 12": "Ada Lovelace Day",
	"oct 13": "International Skeptics Day",
	"oct 15": "I Love Lucy Day",
	"oct 16": "Sweetest Day",
	"oct 16": "Dictionary Day",
	"oct 17": "Wear Something Gaudy Day",
	"oct 18": "Chocolate Cupcake Day",
	"oct 18": "National Clean Out Your Virtual Desktop Day",
	"oct 20": "International Sloth Day",
	"oct 21": "Count your Buttons Day",
	"oct 22": "Caps Lock Day",
	"oct 23": "Mole Day",
	"oct 24": "Bologna Day",
	"oct 25": "Sourest Day",
	"oct 26": "Howl at the Moon Day and Night",
	"oct 27": "American Beer Day",
	"oct 28": "International Animation Day",
	"oct 29": "Internet Day",
	"oct 30": "Candy Corn Day",
	"oct 31": "Magic Day",},
"november":	
	{"nov 1": "Author's Day",
	"nov 2": "Deviled Eggs Day",
	"nov 3": "Sandwich Day",
	"nov 4": "Common Sense Day",
	"nov 4": "Men Make Dinner Day",
	"nov 4": "International Stout Day",
	"nov 6": "Saxophone Day",
	"nov 7": "Zero Tasking Day",
	"nov 7": "Bittersweet Chocolate with Almonds Day",
	"nov 8": "Tongue Twister Day",
	"nov 9": "Chaos Never Dies Day",
	"nov 10": "Forget Me Not Day",
	"nov 10": "Vanilla Cupcake Day",
	"nov 11": "Origami Day",
	"nov 12": "Happy Hour Day",
	"nov 13": "World Kindness Day",
	"nov 13": "Sadie Hawkins Day",
	"nov 14": "Spicy Guacamole Day",
	"nov 14": "Pickle Day",
	"nov 15": "Clean Out Your Refrigerator Day",
	"nov 16": "Fast Food Day",
	"nov 17": "Take A Hike Day",
	"nov 18": "Push Button Phone Day",
	"nov 18": "Use Less Stuff Day",
	"nov 20": "National Absurdity Day",
	"nov 21": "World Hello Day",
	"nov 22": "Go For a Ride Day",
	"nov 23": "Fibonacci Day",
	"nov 24": "Celebrate Your Unique Talent Day",
	"nov 25": "Shopping Reminder Day",
	"nov 26": "Cake Day",
	"nov 26": "Buy Nothing Day",
	"nov 28": "Red Planet Day",
	"nov 29": "Electronic Greeting Card Day",
	"nov 30": "Computer Security Day",},
"december":	
	{"dec 1": "Eat a Red Apple Day",
	"dec 2": "Fritters Day",
	"dec 3": "Make a Gift Day",
	"dec 4": "Wear Brown Shoes Day",
	"dec 5": "Day of the Ninja",
	"dec 6": "Put on Your Own Shoes Day",
	"dec 6": "Microwave Oven Day",
	"dec 7": "Letter Writing Day",
	"dec 8": "Pretend to Be a Time Traveler Day",
	"dec 9": "Christmas Card Day",
	"dec 10": "Dewey decimal System Day",
	"dec 10": "jane Addams Day",
	"dec 10": "Official Lost and Found Day",
	"dec 11": "Noodle Ring Day",
	"dec 12": "Gingerbread House Day",
	"dec 14": "Monkey Day",
	"dec 16": "Chocolate Covered Anything Day",
	"dec 17": "Wright Brothers Day",
	"dec 17": "Underdog Day",
	"dec 17": "Ugly Sweater Day",
	"dec 20": "Sangria Day",
	"dec 21": "International Dalek Remembrance Day",
	"dec 22": "Date Nut Bread Day",
	"dec 23": "Festivus",
	"dec 24": "Eggnog Day",
	"dec 25": "Grav Mass Day",
	"dec 25": "Alphabet Day",
	"dec 26": "Thank You Note Day",
	"dec 27": "No Interruptions Day",
	"dec 28": "Card Playing Day",
	"dec 29": "Pepper Pot Day",
	"dec 30": "Bicarbonate of Soda Day",
	"dec 31": "Make Up Your Mind Day",}
	}

print("I will tell you the weird holiday that falls on your birthday!")
birthday=input("What is your birthday? ")

if birthday:
    
    birthdaylist=birthday.lower().split(" ",1)

    month=birthdaylist[0]
    day=birthdaylist[1]

    shortdate=month[0:3]+" "+day
    holiday=weirdholidays[month].get(shortdate)

    print("The weird holiday on your birthday is......")
    print(f"{holiday}!")
else:
    print("ERROR")


#print(birthdaylist)
#print(month)
#print(day)

#print(weirdholidays["december"].get("dec 25"))
#print(weirdholidays["april"].get("apr 12"))
#print(weirdholidays["january"].get("jan 18"))



