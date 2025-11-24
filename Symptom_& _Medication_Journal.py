# Symptom & Medication Journal
import datetime 
data = [] 

def add_item():
    print("\n--- Add New Item ---")
    name = input("Enter medication or symptom name: ").strip().title()
    
    if not name:
        print("Error: Name cannot be empty.")
        return

    print("Select Category:")
    print("1. Medication")
    print("2. Symptom")
    cat_choice = input("Enter 1 or 2: ")
    
    if cat_choice == '1':
        category = "Medication"
    elif cat_choice == '2':
        category = "Symptom"
    else:
        category = "Unspecified"

    data.append({"name": name, "category": category, "count": 0,"last_logged": "Never"}) 
    print(f"Success: '{name}' added to your tracker!\n")

def log_occurrence():
    if not data:
        print("\n[!] No items to track yet. Please add an item first.\n")
        return
    
    print("\n--- Track Event ---")
    for index, item in enumerate(data, 1):
        print(f"{index}. {item['name']} ({item['category']})")
    
    try:
        choice_index = int(input("\nEnter the number to log: ")) - 1

        if 0 <= choice_index < len(data):
            item = data[choice_index]

            item['count'] += 1

            now = datetime.datetime.now()
            item['last_logged'] = now.strftime("%Y-%m-%d %H:%M")
            
            print(f"Logged: {item['name']} (+1 count)")
        else:
            print("Error: Invalid number selected.")
            
    except ValueError:
        print("Error: Please enter a valid number.")

def view_summary():
    if not data:
        print("\n[!] No records found.\n")
        return
        
    print("\n" + "="*25)
    print(" JOURNAL SUMMARY ")
    print("="*25)
    for item in data:
        print(f"Name: {item['name']}")
        print(f"Type: {item['category']}")
        print(f"Total Events: {item['count']}")
        print(f"Last Event:   {item['last_logged']}")
        print("-" * 15) 
    print()

def menu():
    while True:
        print("===== HEALTH TRACKER =====")
        print("1. Add New Item")
        print("2. Log an Event")
        print("3. View Summary")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            log_occurrence()
        elif choice == '3':
            view_summary()
        elif choice == '4':
            print("Exiting program. Stay healthy!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == '__main__':
    menu()
