import json

class SATResults:
    def _init_(self, name, address, city, country, pincode, sat_score):
        self.name = name
        self.address = address
        self.city = city
        self.country = country
        self.pincode = pincode
        self.sat_score = sat_score
        self.passed = "Pass" if sat_score > 30 else "Fail"

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

def insert_data(records):
    name = input("Enter name: ")
    address = input("Enter address: ")
    city = input("Enter city: ")
    country = input("Enter country: ")
    pincode = input("Enter pincode: ")
    try:
        sat_score = int(input("Enter SAT score: "))
    except ValueError:
        print("Invalid SAT score. Please enter a valid number.")
        return
    record = SATResults(name, address, city, country, pincode, sat_score)
    records.append(record)
    print(f"Data for {name} inserted.")

def view_all_data(records):
    if not records:
        print("No records to display.")
    else:
        for record in records:
            print(f"Name: {record.name}, SAT Score: {record.sat_score}, Passed: {record.passed}")

def get_rank(records, name):
    sorted_records = sorted(records, key=lambda x: x.sat_score, reverse=True)
    for i, record in enumerate(sorted_records):
        if record.name == name:
            print(f"{name} is ranked #{i + 1}")
            return
    print(f"No record found for {name}.")

def update_score(records, name):
    for record in records:
        if record.name == name:
            try:
                new_score = int(input("Enter new SAT score: "))
                record.sat_score = new_score
                record.passed = "Pass" if new_score > 30 else "Fail"
                print(f"Score for {name} updated.")
            except ValueError:
                print("Invalid SAT score. Please enter a valid number.")
            return
    print(f"No record found for {name}.")

def delete_record(records, name):
    for i, record in enumerate(records):
        if record.name == name:
            del records[i]
            print(f"Record for {name} deleted.")
            return
    print(f"No record found for {name}.")

def calculate_average_score(records):
    if not records:
        print("No records available.")
    else:
        avg_score = sum(record.sat_score for record in records) / len(records)
        print(f"Average SAT score: {avg_score:.2f}")

def filter_by_status(records, status):
    filtered_records = [record for record in records if record.passed == status]
    if not filtered_records:
        print(f"No records found with status {status}.")
    else:
        for record in filtered_records:
            print(f"Name: {record.name}, SAT Score: {record.sat_score}, Passed: {record.passed}")

def save_data_to_json(records, filename='sat_results.json'):
    data = [{"name": record.name, "address": record.address, "city": record.city, 
             "country": record.country, "pincode": record.pincode, 
             "sat_score": record.sat_score, "passed": record.passed} for record in records]
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")

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
            status = input("Enter status to filter by (Pass/Fail): ")
            filter_by_status(records, status)
        elif choice == '8':
            save_data_to_json(records)
        elif choice == '9':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

if _name_ == "_main_":
    main()