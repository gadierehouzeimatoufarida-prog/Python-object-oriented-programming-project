print("======================")
print("STUDENT CARD")
print("======================")
greeting=input("How are you ? : ")
print(f"{greeting},Ok")
verif=input("Are you a student ? : ")
#Student informations
student_name=input("Enter your name: ")
student_surname=input("Enter your surname: ")
student_gender=input("Enter your gender: ")
student_weight=float(input("Enter your weight (in kg): "))
student_height=float(input("Enter your height (in meters): "))
student_birth_year=int(input("Enter your birth year: "))
age=2025-student_birth_year
print(f"You are {age} years old")
student_brith_place=input("Enter your birth place: ")
student_phone_number=int(input("Enter your phone number: "))
student_department=input("Enter your department: ")
student_level=int(input("Enter your school level: "))
student_id=input("Enter your id: ")
is_scholarship_holder=bool(input("Are you a scholarship holder ? (yes/no): "))
#Emergency informations 
student_emergency_full_name=input("Enter your emergency full name: ")
student_emergency_phone_number=int(input("Enter your emergency phone number: "))
print("----------------------")
print("Here is your student card ")
print("-----------------------")
print( "Name              : ", student_name)
print( "Surname           : ", student_surname)
print( "Gender            : ", student_gender)
print( "Weight            : ", student_weight, "kg")
print( "Height            : ", student_height, "m")
print( "Age               : ", age)
print( "Phone number      : ", student_phone_number)
print( "Department        : ", student_department)
print( "Id                : ", student_id)
print( "Emergency person  : ", student_emergency_full_name)
print( "Phone number      : ", student_emergency_phone_number)
print("-----------------------")
print(f"You are in {student_level} year level")
year_remain=4-student_level
graduation_year=2025+year_remain
print(f"You will be diplomate in {graduation_year}")
print("======================")
print("END OF THE STUDENT CARD")
print("======================")





