# Class to represent a Doctor with details such as ID, name, specialization, work time, qualification, and room number. - Alessandro
class Doctor:
    def __init__(self, doctor_id, name, specialization, work_time, qualification, room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.work_time = work_time
        self.qualification = qualification
        self.room_number = room_number

    # Getter method for doctor_id - Alessandro
    def get_doctor_id(self):
        return self.doctor_id

    # Setter method for doctor_id - Alessandro
    def set_doctor_id(self, new_doctor_id):
        self.doctor_id = new_doctor_id

    # String representation of a Doctor object - Alessandro
    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.work_time}_{self.qualification}_{self.room_number}"


# Class to represent a Patient with details such as ID, name, disease, gender, and age. - Alessandro
class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    # Getter method for patient ID - Alessandro
    def get_pid(self):
        return self.pid

    # Setter method for patient ID - Alessandro
    def set_pid(self, new_pid):
        self.pid = new_pid

    # String representation of a Patient object - Alessandro
    def __str__(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"


# Main program class that manages the overall menu and user interactions. - Alessandro
class ManagementMethod:
    def __init__(self):
        # Initialize manager objects for doctors and patients - Alessandro
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    # Display the menu options for the user - Alessandro
    def display_menu(self):
        print("\nMenu:")
        print("1. Display Doctors List")  # Option to display all doctors - Alessandro
        print("2. Add Doctor")  # Option to add a new doctor - Alessandro
        print("3. Edit Doctor Info")  # Option to edit an existing doctor's details - Alessandro
        print("4. Display Patients List")  # Option to display all patients - Alessandro
        print("5. Add Patient")  # Option to add a new patient - Alessandro
        print("6. Edit Patient Info")  # Option to edit an existing patient's details - Alessandro
        print("7. Exit")  # Option to exit the program - Alessandro

    # Handle the user's menu choice and call the appropriate method - Alessandro
    def handle_choice(self, choice):
        if choice == "1":
            # Display the list of doctors - Alessandro
            self.doctor_manager.display_doctors_list()
        elif choice == "2":
            # Add a new doctor to the system - Alessandro
            doctor = self.doctor_manager.enter_dr_info()
            self.doctor_manager.add_dr_to_file(doctor)
        elif choice == "3":
            # Edit an existing doctor's information - Alessandro
            doctor_id = input("Enter Doctor ID to edit: ")
            self.doctor_manager.edit_doctor_info(doctor_id)
        elif choice == "4":
            # Display the list of patients - Alessandro
            self.patient_manager.display_patients_list()
        elif choice == "5":
            # Add a new patient to the system - Alessandro
            patient = self.patient_manager.enter_patient_info()
            self.patient_manager.add_patient_to_file(patient)
        elif choice == "6":
            # Edit an existing patient's information - Alessandro
            pid = input("Enter Patient ID to edit: ")
            self.patient_manager.edit_patient_info_by_id(pid)
        elif choice == "7":
            # Exit the program - Alessandro
            print("Exiting program.")
            return False
        else:
            # Handle invalid menu choices - Alessandro
            print("Invalid choice. Please try again.")
        return True

    # Main loop to run the program - Alessandro
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if not self.handle_choice(choice):
                break


# If this script is run directly, start the management system - Alessandro
if __name__ == "__main__":
    system = ManagementMethod()
    system.run()
