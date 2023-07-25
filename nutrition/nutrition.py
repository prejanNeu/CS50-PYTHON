name= input ("Item: ").title()
fruits ={"Apple":"130",
         "Avocado":"50",
         "Sweet Cherries":"100",
         "Kiwifruit":"90",
         "Pear":"100"
}
# if name in fruits.keys():
if name in fruits:
    print("Calories:  "+fruits[name])
    