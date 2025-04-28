# 📊 This program counts how many times each number appears in a list.
# It uses a dictionary to store and update the count of each number.

def count_numbers():
    count_dictionary = {}
    
    print("🔢 Enter numbers one by one. Press Enter without typing to finish.\n")
    
    while True:
        user_input = input("Enter a number: ").strip()
        
        if not user_input:
            break
        
        if not user_input.isdigit():
            print("❌ Invalid input! Please enter a valid number.")
            continue
        
        user_num = int(user_input)
        
        # Update count in dictionary
        count_dictionary[user_num] = count_dictionary.get(user_num, 0) + 1

    # Display the results
    print("\n📈 Result:")
    print("-" * 30)
    if count_dictionary:
        for num, count in sorted(count_dictionary.items()):
            print(f"🔹 {num} appears {count} time{'s' if count > 1 else ''}.")
    else:
        print("⚠️ No numbers were entered.")

def main():
    count_numbers()

if __name__ == "__main__":
    main()
