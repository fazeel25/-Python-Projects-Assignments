# 📱 This program shows an example of using dictionaries to manage a Phonebook.

phonebook = {}

def add_contact():
    """Adds a new contact to the phonebook."""
    while True:
        name = input("✨ Enter contact name: ").strip()
        if not name:
            print("❌ Name cannot be empty. Please enter a valid name.")
            continue
        
        if name in phonebook:
            print("⚠️ Contact already exists! Updating the number.")
        
        while True:
            number = input("📞 Enter contact number: ").strip()
            if not number:
                print("❌ Number cannot be empty. Please enter a valid number.")
                continue
            if not number.isdigit():
                print("🚫 Invalid input. Please enter digits only.")
                continue
            phonebook[name] = number
            print("✅ Contact saved successfully!")
            return

def search_contact():
    """Searches for a contact in the phonebook."""
    search_name = input("🔍 Enter name to search: ").strip()
    if not search_name:
        print("❌ Name cannot be empty.")
        return
    
    for name, number in phonebook.items():
        if name.lower() == search_name.lower():
            print(f"💡 {name}'s number is {number}")
            return
    print(f"😞 {search_name} not found in phonebook.")

def delete_contact():
    """Deletes a contact from the phonebook."""
    delete_name = input("🗑️ Enter name to delete: ").strip()
    if not delete_name:
        print("❌ Name cannot be empty.")
        return
    
    for name in list(phonebook.keys()):
        if name.lower() == delete_name.lower():
            del phonebook[name]
            print(f"🗑️ {name} deleted successfully!")
            return
    print(f"😞 {delete_name} not found in phonebook.")

def show_all():
    """Displays all contacts in the phonebook."""
    if not phonebook:
        print("📭 Phonebook is empty.")
    else:
        print("\n📇 All Contacts:")
        print("-" * 30)
        for name, number in sorted(phonebook.items()):
            print(f"🔸 {name}: {number}")

def main():
    """Main function to run the phonebook program."""
    while True:
        print("\n============================")
        print("📱 Phonebook Menu")
        print("============================")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Show All Contacts")
        print("5. Exit")
        print("============================")

        choice = input("👉 Enter your choice (1-5): ").strip()

        match choice:
            case "1":
                add_contact()
            case "2":
                search_contact()
            case "3":
                delete_contact()
            case "4":
                show_all()
            case "5":
                print("👋 Exiting Phonebook. Goodbye!")
                break
            case _:
                print("❌ Invalid choice! Please select between 1-5.")

if __name__ == "__main__":
    main()
