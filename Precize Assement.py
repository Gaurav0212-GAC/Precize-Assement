import json

# SAT Results class to store data
class SATResults:
    def _init_(self, name, address, city, country, pincode, sat_score):
        self.name = name
        self.address = address
        self.city = city
        self.country = country
        self.pincode = pincode
        self.sat_score = sat_score
        self.passed = "Pass" if sat_score > 30 else "Fail"

# Function to display menu
def display_menu():
    print("\n--- SAT Results Menu ---")
    print("1. Insert data")
    print("2. View all data")
    print("3. Get rank")
    print("4. Update score")
    print("5. Delete one record")
    print("6. Calculate Average SAT Score")
    print("7. Filter records by Pass/Fail Status")
    print("8. Save data to JSON file")
    print("9. Exit")

# Insert data
def insert_data(records):
    name = input("Enter name: ")
    address = input("Enter address: ")
    city = input("Enter city: ")
    country = input("Enter country: ")
    pincode = input("Enter pincode: ")
    sat_score = int(input("Enter SAT score: "))
    record = SATResults(name, address, city, country, pincode, sat_score)
    records.append(record)
    print(f"Data for {name} inserted successfully!")

# View all data
def view_all_data(records):
    data = [vars(record) for record in records]
    print(json.dumps(data, indent=4))

# Get rank
def get_rank(records, name):
    sorted_records = sorted(records, key=lambda x: x.sat_score, reverse=True)
    for i, record in enumerate(sorted_records):
        if record.name == name:
            print(f"{name} is ranked #{i + 1}")
            return
    print("Name not found.")

# Update score
def update_score(records, name):
    for record in records:
        if record.name == name:
            new_score = int(input("Enter new SAT score: "))
            record.sat_score = new_score
            record.passed = "Pass" if new_score > 30 else "Fail"
            print(f"Score for {name} updated successfully!")
            return
    print("Name not found.")

# Delete record
def delete_record(records, name):
    records[:] = [record for record in records if record.name != name]
    print(f"Record for {name} deleted successfully!")

# Calculate average SAT score
def calculate_average_score(records):
    if not records:
        print("No records available to calculate average.")
        return
    avg_score = sum(record.sat_score for record in records) / len(records)
    print(f"Average SAT score: {avg_score:.2f}")

# Filter records by pass/fail status
def filter_by_status(records, status):
    filtered = [record for record in records if record.passed == status]
    if filtered:
        print(f"Records with status {status}:")
        for record in filtered:
            print(vars(record))
    else:
        print(f"No records found with status {status}.")

# Save data to JSON file
def save_data_to_json(records, filename='sat_results.json'):
    data = [vars(record) for record in records]
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")

# Main program loop
def main():
    records = []
    while True:
        display_menu()
        choice = input("Select an option: ")
        if choice == '1':
            insert_data(records)
        elif choice == '2':
            view_all_data(records)
        elif choice == '3':
            name = input("Enter name to get rank: ")
            get_rank(records, name)
        elif choice == '4':
            name = input("Enter name to update score: ")
            update_score(records, name)
        elif choice == '5':
            name = input("Enter name to delete: ")
            delete_record(records, name)
        elif choice == '6':
            calculate_average_score(records)
        elif choice == '7':
            status = input("Filter by (Pass/Fail): ")
            filter_by_status(records, status)
        elif choice == '8':
            save_data_to_json(records)
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if _name_ == "_main_":
    main()
