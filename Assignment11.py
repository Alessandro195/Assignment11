class Doctor:
    def __init__(self, doctor_id, name, specialization, work_time, qualification, room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.work_time = work_time
        self.qualification = qualification
        self.room_number = room_number

    def get_doctor_id(self):
        return self.doctor_id

    def set_doctor_id(self, new_doctor_id):
        self.doctor_id = new_doctor_id

    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.work_time}_{self.qualification}_{self.room_number}"


class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def get_pid(self):
        return self.pid

    def set_pid(self, new_pid):
        self.pid = new_pid

    def __str__(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"

# Main program loop
class ManagementMethod:
    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def display_menu(self):
        print("\nMenu:")
        print("1. Display Doctors List")
        print("2. Add Doctor")
        print("3. Edit Doctor Info")
        print("4. Display Patients List")
        print("5. Add Patient")
        print("6. Edit Patient Info")
        print("7. Exit")

    def handle_choice(self, choice):
        if choice == "1":
            self.doctor_manager.display_doctors_list()
        elif choice == "2":
            doctor = self.doctor_manager.enter_dr_info()
            self.doctor_manager.add_dr_to_file(doctor)
        elif choice == "3":
            doctor_id = input("Enter Doctor ID to edit: ")
            self.doctor_manager.edit_doctor_info(doctor_id)
        elif choice == "4":
            self.patient_manager.display_patients_list()
        elif choice == "5":
            patient = self.patient_manager.enter_patient_info()
            self.patient_manager.add_patient_to_file(patient)
        elif choice == "6":
            pid = input("Enter Patient ID to edit: ")
            self.patient_manager.edit_patient_info_by_id(pid)
        elif choice == "7":
            print("Exiting program.")
            return False
        else:
            print("Invalid choice. Please try again.")
        return True

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if not self.handle_choice(choice):
                break

if __name__ == "__main__":
    system = ManagementMethod()
    system.run()