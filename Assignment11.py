class Doctor:#Alessandro
    # Constructor to initialize doctor details
    def __init__(self, doctor_id, name, specialization, work_time, qualification, room_number):
        # Initialize doctor attributes
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.work_time = work_time
        self.qualification = qualification
        self.room_number = room_number

    # Getter method for doctor ID
    def get_doctor_id(self):
        return self.doctor_id

    # Setter method for doctor ID
    def set_doctor_id(self, new_doctor_id):
        self.doctor_id = new_doctor_id

    # Return a formatted string representation of the doctor object
    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.work_time}_{self.qualification}_{self.room_number}"


class Patient:#Alessandro
    # Constructor to initialize patient details
    def __init__(self, pid, name, disease, gender, age):
        # Initialize patient attributes
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    # Getter method for patient ID
    def get_pid(self):
        return self.pid

    # Setter method for patient ID
    def set_pid(self, new_pid):
        self.pid = new_pid

    # Return a formatted string representation of the patient object
    def __str__(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"


class DoctorManager:
    # Initialize the DoctorManager class
    def __init__(self):# Xander
        self.doctorsList = []  # List to store doctor objects
        self.read_doctors_file()  # Load doctors from file

    # Read doctor details from the file
    def read_doctors_file(self):  # Xander
        with open('doctors.txt') as doctor_file:
            num = 0  # To skip the header line
            for line in doctor_file:
                if num != 0:  # Skip header
                    doc = line.rstrip()
                    docSplit = doc.split('_')  # Split line into attributes
                    id = docSplit[0]
                    name = docSplit[1]
                    specialty = docSplit[2]
                    timing = docSplit[3]
                    qualification = docSplit[4]
                    roomNb = docSplit[5]
                    self.doctorsList.append([id, name, specialty, timing, qualification, roomNb])  # Add doctor details to the list
                num += 1

    # Display all doctors in a formatted table
    def display_doctors_list(self):# Xander
        print("ID   Name                   Specialty        Timing          Qualification   Room Number\n")
        for doc in self.doctorsList:
            print(f"{doc[0]:<5} {doc[1]:<20} {doc[2]:<15} {doc[3]:<15} {doc[4]:<15} {doc[5]} \n")

    # Enter new doctor details interactively
    def enter_dr_info(self):  # Xander
        id = int(input("Enter the doctor’s ID: "))
        name = input("Enter the doctor’s name: ")
        specialty = input("Enter the doctor’s specialty: ")
        timing = input("Enter the doctor’s timing (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor’s qualification: ")
        room_number = int(input("Enter the doctor’s room number: "))
        new_doc_info = [id, name, specialty, timing, qualification, room_number]
        return new_doc_info

    # Add a new doctor to the file
    def add_dr_to_file(self, new_doctor):  # Xander
        self.doctorsList.append(new_doctor)  # Append new doctor to the list
        self.write_list_of_doctors_to_file()  # Save updated list to the file
        print(f"Doctor with ID {new_doctor[0]} has been added.")

    # Write all doctors to the file
    def write_list_of_doctors_to_file(self):# Xander
        with open('doctors.txt', 'w') as doctor_file:
            doctor_file.write("id_name_specialty_timing_qualification_room_number\n")  # Write header line
            for doc in self.doctorsList:
                doctor_file.write(f"{doc[0]}_{doc[1]}_{doc[2]}_{doc[3]}_{doc[4]}_{doc[5]}\n")

    # Search for a doctor by ID
    def search_doctor_by_id(self, doctor_id): #Alessandro
        for doc in self.doctorsList:
            if int(doc[0]) == doctor_id:  # Match ID
                # Print header
                print("\nID   Name                   Specialty        Timing          Qualification   Room Number")
                # Print doctor details in aligned format
                print(f"{doc[0]:<5} {doc[1]:<20} {doc[2]:<15} {doc[3]:<15} {doc[4]:<15} {doc[5]}")
                return doc
        print(f"\nNo doctor found with ID {doctor_id}.")
        return None

    # Edit doctor details by ID
    def edit_doctor_info(self, doctor_id):# Xander
        for doc in self.doctorsList:
            if int(doc[0]) == doctor_id:
                if doc:  # If doctor found
                    doc[1] = input("Enter new Name: ")
                    doc[2] = input("Enter new Specialty: ")
                    doc[3] = input("Enter new Timing: ")
                    doc[4] = input("Enter new Qualification: ")
                    doc[5] = int(input("Enter new Room number: "))
                    self.write_list_of_doctors_to_file()
                    print(f"Doctor with ID {doctor_id} has been edited.")
        print(f"\nNo doctor found with ID {doctor_id}.")
        return None
            
    def search_doctor_by_name(self,name):# Xander
        name=(f"{name}").lower()# Case-insensitive comparison
        for doc in self.doctorsList:
            if (doc[1].lower()).rstrip() == name:
                print("Id    Name                 Speciality      Timing          Qualification   Room Number\n")
                print(f"{(doc)[0]:<5} {(doc)[1]:<20} {(doc)[2]:<15} {(doc)[3]:<15} {(doc)[4]:<15} {(doc)[5]} \n")
                return
        print("Can't find the doctor with the same name on the system.")


class PatientManager:
    # Initialize PatientManager class
    def __init__(self):  # Xander
        self.patientsList = []  # List to store patient objects
        self.read_patients_file()  # Load patients from file

    # Read patient details from the file
    def read_patients_file(self):  # Xander
        with open('patients.txt') as patient_file:
            num = 0  # To skip the header line
            for line in patient_file:
                if num != 0:  # Skip header
                    pat = line.rstrip()
                    patSplit = pat.split('_')  # Split line into attributes
                    id = patSplit[0]
                    name = patSplit[1]
                    disease = patSplit[2]
                    gender = patSplit[3]
                    age = patSplit[4]
                    self.patientsList.append([id, name, disease, gender, age])  # Add patient details to the list
                num += 1

    # Display all patients in a formatted table
    def display_patient_list(self):# Xander
        print("ID   Name                   Disease         Gender          Age\n")
        for pat in self.patientsList:
            print(f"{pat[0]:<5} {pat[1]:<20} {pat[2]:<15} {pat[3]:<15} {pat[4]:<5}\n")

    # Enter new patient details interactively
    def enter_patient_info(self):  # Xander
        id = int(input("Enter Patient ID: "))
        name = input("Enter Patient name: ")
        disease = input("Enter Patient Disease: ")
        gender = input("Enter Patient gender: ")
        age = int(input("Enter Patient age: "))
        new_pat_info = [id, name, disease, gender, age]
        return new_pat_info

    # Add a new patient to the file
    def add_patient_to_file(self, new_patient):  # Xander
        self.patientsList.append(new_patient)  # Append new patient to the list
        self.write_list_of_patients_to_file()  # Save updated list to the file
        print(f"Patient with ID {new_patient[0]} has been added.")

    # Write all patients to the file
    def write_list_of_patients_to_file(self):# Xander
        with open('patients.txt', 'w') as patient_file:
            patient_file.write("id_name_disease_gender_age\n")  # Write header line
            for pat in self.patientsList:
                patient_file.write(f"{pat[0]}_{pat[1]}_{pat[2]}_{pat[3]}_{pat[4]}\n")

    # Search for a patient by ID
    def search_patient_by_id(self, patient_id): #Alessandro
        for pat in self.patientsList:
            if int(pat[0]) == patient_id:  # Match ID
                # Print header
                print("\nID   Name                   Disease         Gender          Age")
                # Print patient details in aligned format
                print(f"{pat[0]:<5} {pat[1]:<20} {pat[2]:<15} {pat[3]:<15} {pat[4]:<5}")
                return pat
        print(f"\nNo patient found with ID {patient_id}.")
        return None

    # Edit patient details by ID
    def edit_patient_info(self, patient_id):# Xander
        for pat in self.patientsList:
            if int(pat[0]) == patient_id:  # Match ID
                if pat:  # If patient found
                    pat[1] = input("Enter new Name: ")
                    pat[2] = input("Enter new Disease: ")
                    pat[3] = input("Enter new Gender: ")
                    pat[4] = int(input("Enter new Age: "))
                    self.write_list_of_patients_to_file()
                    print(f"Patient with ID {patient_id} has been edited.")
        print(f"\nNo patient found with ID {patient_id}.")
        return None


class ManagementMethod:#Alessandro
    def __init__(self):
        # Initialize DoctorManager and PatientManager instances for managing respective operations.
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def display_menu(self):
        # Display the main menu options to the user.
        print("\nWelcome to Alberta Hospital (AH) Management system")
        print("Select from the following options, or select 3 to stop: ")
        print("1 - Doctors")
        print("2 - Patients")
        print("3 - Exit Program")

    def handle_choice(self, choice):
        # Handle the user input from the main menu.
        if choice == "1":
            self.doctor_menu()  # Navigate to the Doctor menu.
        elif choice == "2":
            self.patient_menu()  # Navigate to the Patient menu.
        elif choice == "3":
            # Exit the program gracefully.
            print("Thanks for using the program. Bye!")
            return False
        else:
            # Handle invalid input.
            print("Invalid choice. Please try again.")
        return True  # Return True to keep the program running.

    def doctor_menu(self):
        # Display the Doctor management menu options.
        while True:
            print("\nDoctors Menu:")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add doctor")
            print("5 - Edit doctor info")
            print("6 - Back to the Main Menu")

            # Collect the user's choice for doctor operations.
            choice = input(">>> ")
            if choice == "1":
                self.doctor_manager.display_doctors_list()  # Display all doctors.
            elif choice == "2":
                doc_id = int(input("Enter the doctor ID: "))  # Get doctor ID to search.
                self.doctor_manager.search_doctor_by_id(doc_id)
            elif choice == "3":
                name = input("Enter the doctor name: ")  # Get doctor name to search.
                self.doctor_manager.search_doctor_by_name(name)
            elif choice == "4":
                doctor = self.doctor_manager.enter_dr_info()  # Collect new doctor details.
                self.doctor_manager.add_dr_to_file(doctor)
            elif choice == "5":
                doctor_id = int(input("Please enter the id of the doctor that you want to edit their information: "))
                self.doctor_manager.edit_doctor_info(doctor_id)
            elif choice == "6":
                return  # Return to the main menu.
            else:
                # Handle invalid input.
                print("Invalid choice. Please try again.")

    def patient_menu(self):
        # Display the Patient management menu options.
        while True:
            print("\nPatients Menu:")
            print("1 - Display patients list")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient info")
            print("5 - Back to the Main Menu")

            # Collect the user's choice for patient operations.
            choice = input(">>> ")
            if choice == "1":
                self.patient_manager.display_patient_list()  # Display all patients.
            elif choice == "2":
                patient_id = int(input("Enter the Patient ID: "))  # Get patient ID to search.
                self.patient_manager.search_patient_by_id(patient_id)
            elif choice == "3":
                # Add a new patient to the system.
                patient = self.patient_manager.enter_patient_info()
                self.patient_manager.add_patient_to_file(patient)
            elif choice == "4":
                # Edit patient details based on their ID.
                patient_id = int(input("Please enter the id of the Patient that you want to edit their information: "))
                self.patient_manager.edit_patient_info(patient_id)
            elif choice == "5":
                return  # Return to the main menu.
            else:
                # Handle invalid input.
                print("Invalid choice. Please try again.")

def main():#Alessandro
    management_system = ManagementMethod()
    while True:
        management_system.display_menu()  # Show the main menu.
        user_choice = input("Enter your choice: ")  # Get user input.
        if not management_system.handle_choice(user_choice):  # Process user choice and exit if needed.
            break

if __name__ == "__main__":
    main()
