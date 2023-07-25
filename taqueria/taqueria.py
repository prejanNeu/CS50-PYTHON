item = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

x = 0

while True:
    try:
        name = input("Item: ").title().strip()
        x= x + item[name]
        print(f"Total: ${x:.2f}")
    except EOFError:
        print()
        break
    except KeyError:
        pass