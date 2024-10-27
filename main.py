import os
import re
import random
from pymongo import MongoClient
import pandas as pd
from prettytable import PrettyTable

# Lists of graduation courses for different streams


client = MongoClient('localhost', 27017)
db = client['Apna_hostel']

rooms = db['Rooms']
student = db['student_deteals']
studentlog = db['student_logs']

def verify_user(room_no, password):
    # Query MongoDB to find matching room number and password
    existing_account = studentlog.find_one({"RoomNO": room_no, "password": password})
    
    if existing_account:
        print(f"Login successful for Room No: {room_no}")
        # Fetch all student details
        studentss = list(student.find({}))  # Convert cursor to a list of documents
        
        # Using pandas to create a DataFrame and display data
        df = pd.DataFrame(studentss)
        print("\nStudent Details (Formatted Table using pandas):\n")
        print(df.to_string(index=False))  # Display without the DataFrame index

        # Using PrettyTable to create a terminal-friendly table
        table = PrettyTable()
        if studentss:
            table.field_names = studentss[0].keys()  # Set column headers
            for doc in studentss:
                table.add_row(doc.values())
        
        print("\nStudent Details (Formatted Table using PrettyTable):\n")
        print(table)

    else:
        print("Invalid room number or password!")
        return None



science_graduation_courses = {
    1: "Bachelor of Science (B.Sc.) in Physics",
    2: "Bachelor of Science (B.Sc.) in Chemistry",
    3: "Bachelor of Science (B.Sc.) in Biology",
    4: "Bachelor of Science (B.Sc.) in Mathematics",
    5: "Bachelor of Science (B.Sc.) in Computer Science",
    6: "Bachelor of Science (B.Sc.) in Environmental Science",
    7: "Bachelor of Science (B.Sc.) in Biochemistry",
    8: "Bachelor of Science (B.Sc.) in Biotechnology",
    9: "Bachelor of Science (B.Sc.) in Statistics",
    10: "Bachelor of Science (B.Sc.) in Information Technology",
    11: "Bachelor of Science (B.Sc.) in Microbiology",
    12: "Bachelor of Science (B.Sc.) in Forensic Science",
    13: "Bachelor of Science (B.Sc.) in Nursing",
    14: "Bachelor of Science (B.Sc.) in Psychology",
    15: "Bachelor of Science (B.Sc.) in Zoology",
    16: "Bachelor of Science (B.Sc.) in Geology",
    17: "Bachelor of Science (B.Sc.) in Astronomy",
    18: "Bachelor of Science (B.Sc.) in Agricultural Science",
    19: "Bachelor of Science (B.Sc.) in Physical Education",
    20: "Bachelor of Science (B.Sc.) in Marine Science",
    21: "Bachelor of Science (B.Sc.) in Health Science",
    22: "Bachelor of Science (B.Sc.) in Actuarial Science",
    23: "Bachelor of Science (B.Sc.) in Sports Science",
    24: "Bachelor of Science (B.Sc.) in Molecular Biology",
    25: "Bachelor of Science (B.Sc.) in Computational Science",
    26: "Bachelor of Science (B.Sc.) in Biomedical Science",
    27: "Bachelor of Science (B.Sc.) in Veterinary Science",
    28: "Bachelor of Science (B.Sc.) in Horticulture",
    29: "Bachelor of Science (B.Sc.) in Agricultural Biotechnology",
    30: "Bachelor of Science (B.Sc.) in Food Science and Technology",
    31: "Bachelor of Science (B.Sc.) in Renewable Energy",
    32: "Bachelor of Science (B.Sc.) in Applied Mathematics",
    33: "Bachelor of Science (B.Sc.) in Artificial Intelligence",
    34: "Bachelor of Science (B.Sc.) in Data Science",
    35: "Bachelor of Science (B.Sc.) in Cyber Security",
    36: "Bachelor of Science (B.Sc.) in Pharmacy",
    37: "Bachelor of Science (B.Sc.) in Optometry",
    38: "Bachelor of Science (B.Sc.) in Ergonomics",
    39: "Bachelor of Science (B.Sc.) in Chemistry with Medicinal Chemistry",
    40: "Bachelor of Science (B.Sc.) in Physics with Astrophysics",
    41: "Bachelor of Science (B.Sc.) in Chemistry with Environmental Science",
    42: "Bachelor of Science (B.Sc.) in Marine Biology",
    43: "Bachelor of Science (B.Sc.) in Industrial Chemistry",
    44: "Bachelor of Science (B.Sc.) in Clinical Psychology",
    45: "Bachelor of Science (B.Sc.) in Animal Science",
    46: "Bachelor of Science (B.Sc.) in Environmental Health",
    47: "Bachelor of Science (B.Sc.) in Pharmaceutical Science",
    48: "Bachelor of Science (B.Sc.) in Digital Forensics",
    49: "Bachelor of Science (B.Sc.) in Clinical Laboratory Science",
    50: "Bachelor of Science (B.Sc.) in Geographical Information Science (GIS)"
}

arts_courses = {
    1: "Bachelor of Arts (B.A.) in English Literature",
    2: "Bachelor of Arts (B.A.) in History",
    3: "Bachelor of Arts (B.A.) in Political Science",
    4: "Bachelor of Arts (B.A.) in Sociology",
    5: "Bachelor of Arts (B.A.) in Psychology",
    6: "Bachelor of Arts (B.A.) in Geography",
    7: "Bachelor of Arts (B.A.) in Philosophy",
    8: "Bachelor of Arts (B.A.) in Economics",
    9: "Bachelor of Arts (B.A.) in Fine Arts",
    10: "Bachelor of Arts (B.A.) in Music",
    11: "Bachelor of Arts (B.A.) in Theatre Arts",
    12: "Bachelor of Arts (B.A.) in Dance",
    13: "Bachelor of Arts (B.A.) in Communication Studies",
    14: "Bachelor of Arts (B.A.) in Journalism and Mass Communication",
    15: "Bachelor of Arts (B.A.) in Visual Arts",
    16: "Bachelor of Arts (B.A.) in Media Studies",
    17: "Bachelor of Arts (B.A.) in Women’s Studies",
    18: "Bachelor of Arts (B.A.) in Cultural Studies",
    19: "Bachelor of Arts (B.A.) in International Relations",
    20: "Bachelor of Arts (B.A.) in Liberal Arts"
}

commerce_courses = {
    1: "Bachelor of Commerce (B.Com) in General",
    2: "Bachelor of Commerce (B.Com) in Accounting",
    3: "Bachelor of Commerce (B.Com) in Finance",
    4: "Bachelor of Commerce (B.Com) in Marketing",
    5: "Bachelor of Commerce (B.Com) in Business Management",
    6: "Bachelor of Commerce (B.Com) in Business Administration",
    7: "Bachelor of Commerce (B.Com) in Banking and Insurance",
    8: "Bachelor of Commerce (B.Com) in E-commerce",
    9: "Bachelor of Commerce (B.Com) in International Business",
    10: "Bachelor of Commerce (B.Com) in Taxation",
    11: "Bachelor of Commerce (B.Com) in Human Resource Management",
    12: "Bachelor of Commerce (B.Com) in Financial Markets",
    13: "Bachelor of Commerce (B.Com) in Retail Management",
    14: "Bachelor of Commerce (B.Com) in Logistics and Supply Chain Management",
    15: "Bachelor of Commerce (B.Com) in Event Management",
    16: "Bachelor of Commerce (B.Com) in Sports Management",
    17: "Bachelor of Commerce (B.Com) in Hospitality Management",
    18: "Bachelor of Commerce (B.Com) in Entrepreneurship",
    19: "Bachelor of Commerce (B.Com) in Corporate Secretaryship",
    20: "Bachelor of Commerce (B.Com) in Digital Marketing"
}

def is_valid_email(email):
    # Define the regular expression for a valid email
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Match the regex pattern with the provided email
    if re.match(email_regex, email):
        return True
    return False


def generate_room_number():
    return random.randint(100, 1000)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display_courses(stream):
    if stream.lower() == 's':
        print("\nAvailable Science Graduation Courses:")
        for key, value in science_graduation_courses.items():
            print(f"{key}. {value}")
    elif stream.lower() == 'a':
        print("\nAvailable Arts Graduation Courses:")
        for key, value in arts_courses.items():
            print(f"{key}. {value}")
    elif stream.lower() == 'c':
        print("\nAvailable Commerce Graduation Courses:")
        for key, value in commerce_courses.items():
            print(f"{key}. {value}")
    else:
        print("Invalid stream selected. Please enter S, A, or C.")

def roomnos():
    rooms = random.random(99,1000)
    return rooms

# Main loop
while True:
    print("    ------ Welcome to Apna Hostel ------")
    print("---------------------------------------------")
    print("1) Admission")
    print("2) Students Login Page")
    print("3) Administration")
    print("4) Fee Structure")
    print("More options coming soon....")

    option = int(input("Select the option:-- "))

    if option == 1:
        while True:
            clear_screen()
            reant = "120k"
            print("------- Welcome to Admission Section --------")

            name = input("Enter student name:-- ")
            while True:

                passStream = input("Enter the stream for your 12th pass (S for Science, A for Arts, C for Commerce): ")
                if passStream.lower() == 's':
                    display_courses('s')
                    break
                elif passStream.lower() == 'a':
                    display_courses('a')
                    break
                elif passStream.lower() == 'c':
                    display_courses('c')
                    break
                else:
                    print("Invalid input. Please enter S, A, or C.")
                    continue
        
            course = int(input("Enter the course number you choose:-- "))
            if passStream.lower() == 's':
                Scourse = science_graduation_courses[course]
            elif passStream.lower() == 'c':
                Scourse = arts_courses[course]
            else:
                Scourse = commerce_courses[course]

            
            prast = int(input("Enter your 12th percentage:-- "))
            if prast <=32 and prast <=100:
                print("you are not eligible for admission  because you failed in the exam")
            else:
                prastage = prast
            while True:
                phoneno = input("Enter your phone number (without 0 and +91):-- ")
                if len(phoneno) == 10 and phoneno.isdigit():
                    student_phone_no = phoneno
                    break
                else:
                    print("Invalid phone number. Please enter a 10-digit number.")
            while True:
                studentEmale = input("Enter your email:-")
                if is_valid_email(studentEmale):
                   break
                else:
                    print("Invalid Email")
                    continue

            # Taking Father's details
            father_name = input("Enter father's name:-- ")
            while True:
                father_phone_no = input("Enter father's phone number (without 0 and +91):-- ")
                if len(father_phone_no) == 10 and father_phone_no.isdigit():
                    break
                else:
                    print("Invalid phone number. Please enter a 10-digit number.")
            # Taking Mother's details
            mother_name = input("Enter mother's name:-- ")
            while True:
                mother_phone_no = input("Enter mother's phone number (without 0 and +91):-- ")
                if len(mother_phone_no) == 10 and mother_phone_no.isdigit():
                    break
                else:
                    print("Invalid phone number. Please enter a 10-digit number.")
        

            print("YOUR TOTAL FEE IS 120K FOR 4 YEAR!")
            input("\nPress Enter to continue...")
            print("\n YOU admission is completed" )
            print("your details are:-- ")
            print(f"your name:-{name}")
            print(f"your 12th % :-{prastage}%")
            print(f"your phone_no:-{student_phone_no}")
            print(f"Your Email is  :- {studentEmale}")
            print(f"your father_name:-{father_name}")
            print(f"your father_phone_no:-{father_phone_no}")
            print(f"your mother_name:-{ mother_name}")
            print(f"your mother_phone_no:-{mother_phone_no}")
            print(f"your passStream:-{passStream}")
            print(f"your selected course.:-{Scourse}")
            print(f"your rent is {reant}")
            while True:
                room = generate_room_number()
                existing_room = rooms.find_one({"room": room})  # Corrected key from "rooom" to "room"
                if existing_room:
                    continue  # If the room exists, continue to generate a new one
                else:
                    userroom = room  # If the room is unique, assign it to userroom
                    rooM = {
                        "studentName":name,
                        "Room_no":userroom
                    }
                    rooms.insert_one(rooM)
                    break  # Exit the loop since we have a unique room
            print(f"your room number is :-- {userroom}")

            while True:
                print("-----Create a new password-----")
                newPassword = input("Enter your password: ")
                rePassword = input("Re-enter your password: ") 
                if newPassword == rePassword:
                    print(f"Password successfully set! \n Your password :- -{newPassword}")
                    break
                else:
                    print("Passwords do not match. Please try again.")
                    continue
            
            existing_account4 = studentlog.find_one({"name": name, "phone_number": student_phone_no})
            if existing_account4:
                print("you are already registered,pass enter to exit.. ")
                break
            else:
                student_detealES = {
                    "name":name,
                    "12th%": str(prastage) + "%",
                    "phoneNo.":student_phone_no,
                    "Email":studentEmale,
                    "fatherName":father_name,
                    "fatherPhoneNo.":father_phone_no,
                    "MotherName":mother_name,
                    "MotherPhoneNo.":mother_phone_no,
                    "selectedCourse":Scourse,
                    "reant":reant,
                    "roomNo.":userroom,
                    "Password":newPassword
                }
                student_account = {
                    "name" : name,
                    "Email": studentEmale,
                    "RoomNO":userroom,
                    "password":newPassword
                }
                studentlog.insert_one(student_account)
                student.insert_one(student_detealES)
                print("Press ENTER to exit")
                break
    
    elif option == 2:
        clear_screen()
        print("------Welcome students-----")
        print("-----------------------------")
        room_no = int(input("Enter your room number: "))
        password = input("Enter your password: ")

        # Verify user
        verify_user(room_no, password)


    elif option == 3:
        clear_screen()
        
    
    elif option == 4:
        print("Fee structure section is under construction.")
        input("\nPress Enter to continue...")
        clear_screen()
    else:
        print("Invalid option. Please select a valid option.")()
