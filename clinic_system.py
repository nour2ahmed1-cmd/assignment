import json
import random
import os

# ─────────────────────────────────────────────
#  Global patient list
# ─────────────────────────────────────────────
patients = []
DATA_FILE = "patients.json"


# ─────────────────────────────────────────────
#  Helper utilities
# ─────────────────────────────────────────────

def generate_unique_id():
    """Generate a random 4-digit ID that doesn't already exist."""
    existing_ids = [p["id"] for p in patients]
    while True:
        new_id = random.randint(0000, 9999)
        if new_id not in existing_ids:
            return new_id


def find_patient_by_id(patient_id):
    """Return the patient dict whose id matches, or None."""
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    return None

def get_patient_by_input(prompt="Enter patient ID: "):
    try:
        patient_id = int(input(prompt).strip())
    except ValueError:
        print("  ⚠  Invalid ID. Please enter a number.")
        return None

    patient = find_patient_by_id(patient_id)
    if not patient:
        print(f"  ⚠  No patient found with that ID.")
        return None

    return patient


def find_patients_by_name(search_name):
    """Return a list of patients whose name contains the search string."""
    return [
        p for p in patients
        if search_name.lower() in p["name"].lower()
    ]


def validate_full_name(name):
    """Name must contain at least two words (first + last)."""
    parts = name.strip().split()
    return len(parts) >= 2


def validate_phone(phone):
    """Phone must be exactly 10 digits."""
    return phone.isdigit() and len(phone) == 10


def validate_age(age_str):
    """
    Accept age in two formats:
      • plain integer  → years  (1 – 120)
      • 'Xm'           → months (1 – 11)
    Returns (age_value, unit) or raises ValueError.
    """
    age_str = age_str.strip().lower()
    if age_str.endswith("m"):
        months = int(age_str[:-1])
        if months < 1 or months > 11:
            raise ValueError("Months must be between 1 and 11.")
        return months, "months"
    else:
        years = int(age_str)
        if years < 1 or years > 120:
            raise ValueError("Age in years must be between 1 and 120.")
        return years, "years"


def validate_symptoms(symptoms):
    """Symptoms must contain 'and' or ',' separating multiple terms, or a single word."""
    return len(symptoms.strip()) > 0


def print_divider():
    print("-" * 40)


def display_patient(patient):
    print(f"  ID      : {patient['id']}")
    print(f"  Name    : {patient['name']}")
    age_display = (
        f"{patient['age']} {patient['age_unit']}"
        if "age_unit" in patient
        else str(patient["age"])
    )
    print(f"  Age     : {age_display}")
    print(f"  Phone   : {patient['phone']}")
    print(f"  Symptoms: {patient['symptoms']}")


# ─────────────────────────────────────────────
#  1. Add New Patient
# ─────────────────────────────────────────────

def add_patient():
    print("\n====== Add New Patient ======")

    # Name
    while True:
        name = input("Enter full name (first and last): ").strip().title()
        if validate_full_name(name):
            break
        print("  ⚠  Please enter a full name (at least first and last name).")

    # Age
    while True:
        try:
            age_input = input("Enter age (e.g. 25 for years, or 8m for months): ")
            age_value, age_unit = validate_age(age_input)
            break
        except ValueError as e:
            print(f"  ⚠  Invalid age: {e}")

    # Phone
    while True:
        phone = input("Enter phone number (10 digits): ").strip()
        if validate_phone(phone):
            break
        print("  ⚠  Phone number must be exactly 10 digits.")

    # Symptoms
    while True:
        symptoms = input("Enter symptoms (use 'and' or ',' between multiple): ").strip()
        if validate_symptoms(symptoms):
            break
        print("  ⚠  Symptoms cannot be empty.")

    patient_id = generate_unique_id()

    new_patient = {
        "id": patient_id,
        "name": name,
        "age": age_value,
        "age_unit": age_unit,
        "phone": phone,
        "symptoms": symptoms,
        "visits": []
    }

    patients.append(new_patient)
    print(f"\n  ✔  Patient '{name}' added successfully with ID: {patient_id}")


# ─────────────────────────────────────────────
#  2. View All Patients
# ─────────────────────────────────────────────

def view_patients():
    print("\n====== All Patients ======")
    if not patients:
        print("  No patients found.")
        return

    for patient in patients:
        print_divider()
        display_patient(patient)
    print_divider()
    print(f"  Total patients: {len(patients)}")


# ─────────────────────────────────────────────
#  3. Search Patient
# ─────────────────────────────────────────────

def search_patient():
    print("\n====== Search Patient ======")
    query = input("Enter patient name or ID: ").strip()

    # Try searching by ID first
    if query.isdigit():
        patient = find_patient_by_id(int(query))
        if patient:
            print("\n  Patient found:")
            print_divider()
            display_patient(patient)
            print_divider()
            return
        else:
            print(f"  ⚠  No patient found with ID: {query}")

    # Search by name
    results = find_patients_by_name(query)
    if results:
        print(f"\n  {len(results)} patient(s) found:")
        for patient in results:
            print_divider()
            display_patient(patient)
        print_divider()
    else:
        print(f"  ⚠  No patient found matching '{query}'.")


# ─────────────────────────────────────────────
#  4. Update Patient Information
# ─────────────────────────────────────────────

def update_patient():
    print("\n====== Update Patient Information ======")

    patient = get_patient_by_input("Enter patient ID to update: ")
    if not patient:
        return

    print(f"\n  Updating: {patient['name']}")
    print("  What do you want to update?")
    print("    1. Name")
    print("    2. Age")
    print("    3. Phone")
    print("    4. Symptoms")

    choice = input("  Choose an option: ").strip()

    if choice == "1":
        while True:
            new_name = input("  Enter new full name: ").strip().title()
            if validate_full_name(new_name):
                patient["name"] = new_name
                break
            print("  ⚠  Please enter a full name (first and last).")

    elif choice == "2":
        while True:
            try:
                age_input = input("  Enter new age (e.g. 30 or 5m): ")
                age_value, age_unit = validate_age(age_input)
                patient["age"] = age_value
                patient["age_unit"] = age_unit 
                break
            except ValueError as e:
                print(f"  ⚠  {e}")

    elif choice == "3":
        while True:
            new_phone = input("  Enter new phone number (10 digits): ").strip()
            if validate_phone(new_phone):
                patient["phone"] = new_phone
                break
            print("  ⚠  Phone must be exactly 10 digits.")

    elif choice == "4":
        while True:
            new_symptoms = input("  Enter new symptoms: ").strip()
            if validate_symptoms(new_symptoms):
                patient["symptoms"] = new_symptoms
                break
            print("  ⚠  Symptoms cannot be empty.")

    else:
        print("  ⚠  Invalid choice.")
        return

    print("  ✔  Patient updated successfully.")


# ─────────────────────────────────────────────
#  5. Add Visit Note
# ─────────────────────────────────────────────

def add_visit_note():
    print("\n====== Add Visit Note ======")

    patient = get_patient_by_input("Enter patient ID to update: ")
    if not patient:
        return
    
    print(f"\n  Adding visit for: {patient['name']}")

    date = input("  Enter visit date (YYYY-MM-DD): ").strip()
    if not date:
        print("  ⚠  Date cannot be empty.")
        return

    doctor = input("  Enter doctor name: ").strip().title()
    if not doctor:
        print("  ⚠  Doctor name cannot be empty.")
        return

    note = input("  Enter visit note: ").strip()
    if not note:
        print("  ⚠  Visit note cannot be empty.")
        return

    advice = input("  Enter prescription / advice: ").strip()
    if not advice:
        print("  ⚠  Advice cannot be empty.")
        return

    visit = {
        "date": date,
        "doctor": doctor,
        "note": note,
        "advice": advice
    }

    patient["visits"].append(visit)
    print("  ✔  Visit note added successfully.")


# ─────────────────────────────────────────────
#  6. View Patient History
# ─────────────────────────────────────────────

def view_patient_history():
    print("\n====== View Patient History ======")

    patient = get_patient_by_input("Enter patient ID: ")
    if not patient:
        return

    print(f"\n  Patient: {patient['name']}")

    if not patient["visits"]:
        print("  No visit history found.")
        return

    for i, visit in enumerate(patient["visits"], start=1):
        print_divider()
        print(f"  Visit {i}:")
        print(f"    Date   : {visit['date']}")
        print(f"    Doctor : {visit['doctor']}")
        print(f"    Note   : {visit['note']}")
        print(f"    Advice : {visit['advice']}")
    print_divider()


# ─────────────────────────────────────────────
#  7. Save Data
# ─────────────────────────────────────────────

def save_data():
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(patients, file, indent=4)
        print(f"  ✔  Data saved successfully to '{DATA_FILE}'.")
    except Exception as e:
        print(f"  ⚠  Could not save data: {e}")


# ─────────────────────────────────────────────
#  8. Load Data
# ─────────────────────────────────────────────

def load_data():
    global patients
    if not os.path.exists(DATA_FILE):
        print("  No saved data found. Starting with an empty system.")
        return

    try:
        with open(DATA_FILE, "r") as file:
            patients = json.load(file)
        print(f"  ✔  Loaded {len(patients)} patient(s) from saved data.")
    except (json.JSONDecodeError, Exception) as e:
        print(f"  ⚠  Could not load data: {e}. Starting fresh.")
        patients = []


# ─────────────────────────────────────────────
#  Advanced Optional Features
# ─────────────────────────────────────────────

def delete_patient():
    print("\n====== Delete Patient ======")

    patient = get_patient_by_input("Enter patient ID to delete: ")
    if not patient:
        return

    confirm = input(f"  Are you sure you want to delete '{patient['name']}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        patients.remove(patient)
        print("  ✔  Patient deleted successfully.")
    else:
        print("  Deletion cancelled.")


def show_statistics():
    print("\n====== Clinic Statistics ======")
    total = len(patients)
    print(f"  Total patients : {total}")

    if total == 0:
        return

    adults   = sum(1 for p in patients if p.get("age_unit", "years") == "years" and p["age"] >= 18)
    children = sum(1 for p in patients if p.get("age_unit") == "months" or
                   (p.get("age_unit", "years") == "years" and p["age"] < 18))
    no_visits = sum(1 for p in patients if len(p["visits"]) == 0)

    print(f"  Adults         : {adults}")
    print(f"  Children       : {children}")
    print(f"  No visits yet  : {no_visits}")


def search_by_symptom():
    print("\n====== Search by Symptom ======")
    symptom = input("Enter symptom to search: ").strip().lower()
    results = [p for p in patients if symptom in p["symptoms"].lower()]

    if results:
        print(f"\n  {len(results)} patient(s) with '{symptom}':")
        for patient in results:
            print_divider()
            display_patient(patient)
        print_divider()
    else:
        print(f"  ⚠  No patients found with symptom '{symptom}'.")


def sort_patients_by_name():
    print("\n====== Patients Sorted by Name ======")
    if not patients:
        print("  No patients to display.")
        return

    sorted_list = sorted(patients, key=lambda p: p["name"])
    for patient in sorted_list:
        print_divider()
        display_patient(patient)
    print_divider()


def export_report():
    print("\n====== Export Report ======")
    report_file = "clinic_report.txt"
    try:
        with open(report_file, "w") as f:
            f.write("====== Clinic Patient Report ======\n\n")
            f.write(f"Total Patients: {len(patients)}\n")
            f.write("=" * 40 + "\n\n")
            for patient in patients:
                f.write(f"ID      : {patient['id']}\n")
                f.write(f"Name    : {patient['name']}\n")
                age_display = f"{patient['age']} {patient.get('age_unit', 'years')}"
                f.write(f"Age     : {age_display}\n")
                f.write(f"Phone   : {patient['phone']}\n")
                f.write(f"Symptoms: {patient['symptoms']}\n")
                f.write(f"Visits  : {len(patient['visits'])}\n")
                f.write("-" * 40 + "\n")
        print(f"  ✔  Report exported to '{report_file}'.")
    except Exception as e:
        print(f"  ⚠  Could not export report: {e}")


# ─────────────────────────────────────────────
#  Main Menu
# ─────────────────────────────────────────────

def show_menu():
    print("\n====== Clinic Patient Management System ======")
    print("  1. Add New Patient")
    print("  2. View All Patients")
    print("  3. Search Patient")
    print("  4. Update Patient Information")
    print("  5. Add Visit Note")
    print("  6. View Patient History")
    print("  7. Save Data")
    print("  8. Delete Patient")
    print("  9. Clinic Statistics")
    print("  10. Search by Symptom")
    print("  11. Sort Patients by Name")
    print("  12. Export Report to File")
    print("  ──────────────────────────────────────")
    print("  0. Exit")
    print("=" * 46)


def main():
    print("\n  Welcome to the Clinic Patient Management System")
    load_data()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            update_patient()
        elif choice == "5":
            add_visit_note()
        elif choice == "6":
            view_patient_history()
        elif choice == "7":
            save_data()
        elif choice == "8":
            delete_patient()
        elif choice == "9":
            show_statistics()
        elif choice == "10":
            search_by_symptom()
        elif choice == "11":
            sort_patients_by_name()
        elif choice == "12":
            export_report()
        elif choice == "0":
            save_choice = input("\n  Do you want to save data before exiting? (yes/no): ").strip().lower()
            if save_choice == "yes":
                save_data()
            print("\n  Thank you for using the Clinic Patient Management System.")
            print("  Goodbye!\n")
            break
        else:
            print("  ⚠  Invalid choice. Please enter a number from the menu.")


# ─────────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────────
main()