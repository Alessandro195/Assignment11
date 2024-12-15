# Define a class for Doctor
class Doctor:
    def __init__(self, id, name, specialty, timing, qualification, room_number):
        # Initialize doctor attributes
        self.id = id
        self.name = name
        self.specialty = specialty
        self.timing = timing
        self.qualification = qualification
        self.room_number = room_number

    def display(self):
        # Display doctor information in a formatted string
        return f"{self.id:<5} {self.name:<20} {self.specialty:<15} {self.timing:<15} {self.qualification:<15} {self.room_number:<10}"

# Define a class for Patient
class Patient:
    def __init__(self, id, name, disease, gender, age):
        # Initialize patient attributes
        self.id = id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def display(self):
        # Display patient information in a formatted string
        return f"{self.id:<5} {self.name:<20} {self.disease:<15} {self.gender:<15} {self.age:<10}"

# Initialize sample data for doctors and patients
doctors = [
    Doctor(21, "Dr.Gody", "ENT", "5am-11am", "MBBS,MD", 17),
    Doctor(32, "Dr.Vikram", "Physician", "10pm-3am", "MBBS,MD", 45),
    Doctor(17, "Dr.Amy", "Surgeon", "8pm-2am", "BDM", 8),
    Doctor(33, "Dr.David", "Artho", "10am-4pm", "MBBS,MS", 40),
    Doctor(123, "Dr. Ross", "Headackes", "8pm-10am", "MST", 102),
    Doctor(66, "Dr. Mike", "Heart", "9am-5pm", "MS", 2)
]

patients = [
    Patient(12, "Pankaj", "Cancer", "Male", 30),
    Patient(13, "Janina", "Cold", "Female", 23),
    Patient(14, "Alonna", "Malaria", "Female", 45),
    Patient(15, "Ravi", "Diabetes", "Male", 65)
]

# Function to display a menu and get user choice
def display_menu(title, options):
    print(f"\n{title} Menu:")
    for i, option in enumerate(options, start=1):
        print(f"{i} - {option}")
    return int(input(">>> "))

# Display all doctors
def display_doctors():
    print("\nId    Name                 Speciality      Timing          Qualification   Room Number")
    for doctor in doctors:
        print(doctor.display())

# Search for a doctor by ID
def search_doctor_by_id():
    id = int(input("\nEnter the doctor Id: "))
    for doctor in doctors:
        if doctor.id == id:
            print("\nId    Name                 Speciality      Timing          Qualification   Room Number")
            print(doctor.display())
            return
    print("Can't find the doctor with the same ID on the system")

# Search for a doctor by name
def search_doctor_by_name():
    name = input("\nEnter the doctor name: ").strip()
    for doctor in doctors:
        if doctor.name == name:
            print("\nId   Name                   Speciality      Timing          Qualification   Room Number")
            print(doctor.display())
            return
    print("Can't find the doctor with the same name on the system")

# Add a new doctor to the list
def add_doctor():
    id = int(input("Enter the doctor's ID: "))
    name = input("Enter the doctor's name: ")
    specialty = input("Enter the doctor's specialty: ")
    timing = input("Enter the doctor's timing (e.g., 7am-10pm): ")
    qualification = input("Enter the doctor's qualification: ")
    room_number = int(input("Enter the doctor's room number: "))
    doctors.append(Doctor(id, name, specialty, timing, qualification, room_number))
    print(f"\nDoctor whose ID is {id} has been added")

# Edit an existing doctor's information
def edit_doctor():
    id = int(input("\nPlease enter the id of the doctor that you want to edit their information: "))
    for doctor in doctors:
        if doctor.id == id:
            doctor.name = input("Enter new Name: ")
            doctor.specialty = input("Enter new Specialty: ")
            doctor.timing = input("Enter new Timing: ")
            doctor.qualification = input("Enter new Qualification: ")
            doctor.room_number = int(input("Enter new Room number: "))
            print(f"\nDoctor whose ID is {id} has been edited")
            return
    print("Can't find the doctor with the same ID on the system")

# Display all patients
def display_patients():
    print("\nID    Name                 Disease         Gender          Age")
    for patient in patients:
        print(patient.display())

# Search for a patient by ID
def search_patient_by_id():
    id = int(input("\nEnter the Patient Id: "))
    for patient in patients:
        if patient.id == id:
            print("\nID    Name                 Disease         Gender          Age")
            print(patient.display())
            return
    print("Can't find the Patient with the same id on the system")

# Add a new patient to the list
def add_patient():
    id = int(input("Enter Patient id: "))
    name = input("Enter Patient name: ")
    disease = input("Enter Patient disease: ")
    gender = input("Enter Patient gender: ")
    age = int(input("Enter Patient age: "))
    patients.append(Patient(id, name, disease, gender, age))
    print(f"\nPatient whose ID is {id} has been added.")

# Edit an existing patient's information
def edit_patient():
    id = int(input("\nPlease enter the id of the Patient that you want to edit their information: "))
    for patient in patients:
        if patient.id == id:
            patient.name = input("Enter new Name: ")
            patient.disease = input("Enter new Disease: ")
            patient.gender = input("Enter new Gender: ")
            patient.age = int(input("Enter new Age: "))
            print(f"\nPatient whose ID is {id} has been edited.")
            return
    print("Can't find the Patient with the same id on the system")

# Main program loop
while True:
    # Display main menu
    choice = display_menu("Welcome to Alberta Hospital (AH) Management system", ["Doctors", "Patients", "Exit Program"])

    if choice == 1:
        # Doctors menu
        while True:
            doctor_choice = display_menu("Doctors", ["Display Doctors list", "Search for doctor by ID", "Search for doctor by name", "Add doctor", "Edit doctor info", "Back to the Main Menu"])

            if doctor_choice == 1:
                display_doctors()
            elif doctor_choice == 2:
                search_doctor_by_id()
            elif doctor_choice == 3:
                search_doctor_by_name()
            elif doctor_choice == 4:
                add_doctor()
            elif doctor_choice == 5:
                edit_doctor()
            elif doctor_choice == 6:
                break
    elif choice == 2:
        # Patients menu
        while True:
            patient_choice = display_menu("Patients", ["Display patients list", "Search for patient by ID", "Add patient", "Edit patient info", "Back to the Main Menu"])

            if patient_choice == 1:
                display_patients()
            elif patient_choice == 2:
                search_patient_by_id()
            elif patient_choice == 3:
                add_patient()
            elif patient_choice == 4:
                edit_patient()
            elif patient_choice == 5:
                break
    elif choice == 3:
        # Exit program
        print("Thanks for using the program. Bye!")
        break
