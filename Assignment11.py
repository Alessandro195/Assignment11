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
class doctormanager: 
    def __init__(self):#Xander
        self.doctorsList=list(" ")
        self.read_doctors_file()
        self.doctorsList.remove(' ')
        
    def format_dr_info(self):#Xander
        formatedList=list(' ')
        for doc in self.doctorsList:
            doc= str(f"{doc[0]}_{doc[1]}_{doc[2]}_{doc[3]}_{doc[4]}_{doc[5]}")
            formatedList.append(doc)
        formatedList.remove(' ')
        return formatedList


    def enter_dr_info(self):#xander
        id = int(input("Enter the doctor's ID: "))
        name = input("Enter the doctor's name: ")
        specialty = input("Enter the doctor's specialty: ")
        timing = input("Enter the doctor's timing (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor's qualification: ")
        room_number = int(input("Enter the doctor's room number: "))
        new_doc_info=(id,name,specialty,timing,qualification,room_number)
        return new_doc_info
    
    def read_doctors_file(self):#Xander
        with open('doctors.txt') as doctor:
            num=0
            for line in doctor:
                if num != 0:
                    doc = line.rstrip()
                    docSplit=list(doc.split('_'))
                    id = docSplit[0]
                    name = docSplit[1]
                    specilist = docSplit[2]
                    timing = docSplit[3]
                    qualification = docSplit[4]
                    roomNb = docSplit[5]
                    # doctor(id,name,specilist,timing,qualification,roomNb)
                    self.doctorsList.append(docSplit)
                num=num+1
                       
    def search_doctor_by_id():
        id = int(input("\nEnter the doctor Id: "))
        
        print("Can't find the doctor with the same ID on the system")
    
    def search_doctor_by_name():
        name = input("\nEnter the doctor name: ").strip()

        print("\nId   Name                   Speciality      Timing          Qualification   Room Number")
        return
    
    def display_doctor_info(self):#Xander
        print("Id    Name                 Speciality      Timing          Qualification   Room Number\n")
        for doc in self.doctorsList:
            print(f"{(doc)[0]:<5} {(doc)[1]:<20} {(doc)[2]:<15} {(doc)[3]:<15} {(doc)[4]:<15} {(doc)[5]} \n")

    
    def edit_doctor_info(self):
        return
    
    def display_doctors_list():
        return
    
    def Write_list_of_doctors_to_file():
        return
    
    def add_dr_to_file(self): #Xander
        new_doc=self.enter_dr_info()
        self.doctorsList.append([new_doc[0],new_doc[1],new_doc[2],new_doc[3],new_doc[4],new_doc[5]])
        formatedList=self.format_dr_info()
        with open('doctors.txt','w') as doctor:
            doctor.write("id_name_specilist_timing_qualification_roomNb\n")
            for doc in formatedList:
                print(doc)
                doctor.writelines(f"{doc}\n")
        print(f"Doctor whose ID is {new_doc[0]} has been added")
        
if __name__ == "__main__": 
    system = ManagementMethod()
    system.run()
