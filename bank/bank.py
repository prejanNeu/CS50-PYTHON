greet = input("Greeting: ").lower().strip().replace(",", " " )
all_word = greet.split()
first_word=all_word[0]
if  first_word== "hello":
    print("$0")
elif first_word.startswith("h"):
    print("$20")
else:
    print("$100")