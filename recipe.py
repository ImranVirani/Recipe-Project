'''
Purpose: Help a user plan a meal using a recipe, asking user to set a date of party, 
date of purchasing ingredients and asking for number. It also provides preparation
and steps to cook Chicken Curry.
STATUS: REVIEW
Author: Imran Virani
'''

print("Welcome to Recipe Calculator! We will be Making Chicken Curry!")
print("---------------------")
# Asks user for date of dinner party, what day the user will be shopping for ingredients and how many servings the meal is for
DateOfParty = input("What is the date of the dinner party? ")
DateOfGroceryShopping = input("What day do you want to go shopping? ")
NumberOfServings = eval(input("How many people are coming? "))
# Calculates the amount per person, assigns variables to each ingredients, 
# each unit for each ingredient and the amount of each ingredient
amountPerPerson = (NumberOfServings / 4)
cookingOil = "Olive Oil"
amountOfCookingOil = 3
unitCookingOil = "tablespoons"
onion = "White Onions"
preparedOnion = "chopped onion"
amountOfOnion = 1
unitOnion = "whole onions"
preparedGarlic = "minced garlic"
garlic = " garlic"
amountOfGarlic = 2
unitGarlic = "cloves"
curryPowder= "curry powder"
amountOfCurryPowder = 3
unitCurryPowder = "tablespoons"
spice1 = "cinnamon"
amountOfSpice1 = 1
unitSpice1 = "tablespoons"
spice2 = "paprika"
amountOfSpice2 = 1
unitSpice2 = "teaspoons"
bayLeaf = "Bay Leaves"
unitBayLeaf = "whole"
amountOfBayLeaves = 1
unitBayLeaves = "Leaves"
ginger = "ginger"
amountOfGingerRoot = 0.5
unitGinger = "roots"
sugar = "white sugar"
amountOfSugar = 0.5
unitSugar = "teaspoons"
meat = "Chicken Breasts"
amountOfMeat = 2
unitMeat = "halves"
paste = "Tomato Paste"
amountOfPaste = 1
unitPaste = "tablespoons"
yogurt = "Plain Yogurt"
amountOfYogurt = 1
unitYogurt = "cups"
milk = "Coconut Milk"
amountOfMilk = 0.75
unitMilk = "cups"
citrusFruit = "hWole Lemons"
preparedCitrus = "Juiced Lemons"
amountOfCitricFruit = 0.5
unitCitrusFruit = "whole lemons"
spicyPepper = "cayenne pepper"
amountOfSpicyPepper = 0.5
unitSpicyPepper = "teaspoons"
totalAmountCookingOil = (NumberOfServings * amountOfCookingOil)
totalAmountOnion = (NumberOfServings * amountOfOnion)
totalAmountGarlic = (NumberOfServings * amountOfGarlic)
totalAmountCurryPowder = (NumberOfServings * amountOfCurryPowder)
totalAmountSpice1 = (NumberOfServings * amountOfSpice1)
totalAmountSpice2 = (NumberOfServings * amountOfSpice2)
totalAmountBayLeaf = (NumberOfServings * amountOfBayLeaves)
totalAmountGinger = (NumberOfServings * amountOfGingerRoot)
totalAmountSugar = (NumberOfServings * amountOfSugar)
totalAmountMeat = (NumberOfServings * amountOfMeat)
totalAmountPaste = (NumberOfServings * amountOfPaste)
totalAmountYogurt = (NumberOfServings * amountOfYogurt)
totalAmountMilk = (NumberOfServings * amountOfMilk)
totalAmountCitrusFruit = (NumberOfServings * amountOfCitricFruit)
totalAmountSpicyPepper = (NumberOfServings * amountOfSpicyPepper)
print("")
print("We will be Making Chicken Curry! This recipe was sourced from allrecipies at https:**www.allrecipes.com*recipe*46822*indian-chicken-curry-ii*")
print("")
print("The date of the dinner party is: " + DateOfParty)
print("Please purchase the following items on " + DateOfGroceryShopping + ":")
# States the amounts of each ingredient for a custom amount of servings stated before
print(str(totalAmountCookingOil) + unitCookingOil + " of " + cookingOil)
print(str(totalAmountOnion) + unitOnion + onion)
print(str(totalAmountGarlic) + unitGarlic + garlic)
print(str(totalAmountCurryPowder) +  unitCurryPowder + "of" + curryPowder)
print(str(totalAmountSpice1) + unitSpice1 + "of" + spice1)
print(str(totalAmountSpice2)+ unitSpice2 + "of" + spice2)
print(str(totalAmountBayLeaf) + unitBayLeaves + "of  " + bayLeaf)
print(str(totalAmountGinger) + " ginger roots")
print(str(totalAmountSugar) + " " + unitSugar + "of " + sugar)
print("")
print(" salt, whatever you have at home(use good judgement)")
print(str(totalAmountMeat) + meat + "halves")
print(str(totalAmountPaste) + unitPaste + " of " + paste)
print(str(totalAmountCitrusFruit) + unitCitrusFruit + citrusFruit)
print("")
# Listing the steps needed to make the dish
print("------How to Make Chicken Curry!------")
# Preparation
print("----------PREPARATION----------")
print("1. Measure " + cookingOil)
print("2. Chop up " + onion + "s")
print("3. Mince" + garlic)
print("4. Measure curry powder")
print("5. Measure" + spice2)
print("6. Set aside your" + bayLeaf)
print("7. Grate" + ginger + "roots")
print("8. Measure sugar")
print("9. Cut your" + meat + "into halves")
print("10. Juice your" + citrusFruit)
print("11. Measure your" + spice1)
# How to cook meal
print("")
print("----------Time to Cook!----------")
print("Step 1: Heat " + str(totalAmountCookingOil)+ " " + unitCookingOil + "of" + cookingOil)
print("in a skillet over medium heat")
print("Step 2: Add" + onion + "to skillet")
print("Step 2: Saute " + preparedOnion + " until lightly browned")
print("Step 3: Stir in " + str(totalAmountGarlic) + " " + unitGarlic + " of " + preparedGarlic)
print(" " + str(totalAmountCurryPowder) + " " + unitCurryPowder + "of" + curryPowder)
print(" " + str(totalAmountSpice1) + str(totalAmountSpice2))
print(" teaspoons of paprika, " + str(totalAmountBayLeaf) + bayLeaf)
print(str(totalAmountGinger) + ginger + unitGinger)
print(str(totalAmountSugar) + sugar + ", and salt")
print("Step 4: Continue stirring for 2 minutes.")
print("Step 5: Add the " + str(totalAmountMeat) + " " + meat + " " + unitMeat + ",")
print(str(totalAmountPaste) + " " + unitPaste + " " + paste + ", " + str(totalAmountYogurt))
print(unitYogurt + " " + yogurt + ", and " + str(totalAmountMilk) + " " + unitMilk + " "+ milk)
print("Step 6: Bring to a boil and reduce heat to low")
print("Step 7: Let it simmer for 20 to 25 minutes.")
print("Step 8: Remove " + " " + str(totalAmountBayLeaf) + " " + unitBayLeaf + " " + bayLeaf)
print(" and stir in " + str(totalAmountCitrusFruit) + " " + preparedCitrus + " and")
print(str(totalAmountSpicyPepper) + " " + unitSpicyPepper + " of " + spicyPepper) 
print("Step 9: Simmer for 5 more minutes.")
print("")
print("YOU'RE DONE! ENJOY! Thank you for using Recipe Calculator")
print("test line")