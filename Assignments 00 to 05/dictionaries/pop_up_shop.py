# 🍎 Fruit Shop Purchase Calculator

fruits = {
    "apple": 10.0,
    "durian": 50.0,
    "jackfruit": 20.0,
    "kiwi": 5.0,
    "rambutan": 15.0,
    "mango": 8.0
}

def main():
    total = 0.0
    print("🍇 Welcome to the Fruit Shop!\n")

    for fruit, price_per_unit in fruits.items():
        while True:
            quantity_input = input(f"How many {fruit}(s) do you want to buy? (Enter 0 if none): ").strip()
            if not quantity_input.isdigit():
                print("❌ Please enter a valid non-negative integer.")
                continue
            quantity = int(quantity_input)
            if quantity < 0:
                print("❌ Quantity cannot be negative.")
                continue
            break
        
        cost = price_per_unit * quantity
        total += cost

    print("\n===============================")
    print(f"🛒 Your total bill is: **${total:.2f}**")
    print("🎉 Thank you for shopping with us!")
    print("===============================\n")

if __name__ == "__main__":
    main()
