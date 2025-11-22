from datetime import datetime

def ask_yes_no(question):
    while True:
        answer = input(question + " (yes/no): ").lower()
        if answer in ("yes", "no"):
            return answer == "yes"
        print("Please answer only yes or no.")

class Student:
    def __init__(self):
        print("======================")
        print("STUDENT CARD")
        print("======================")

        greeting = input("How are you ? : ")
        print(f"{greeting}, Ok")

        is_student = ask_yes_no("Are you a student ?")
        if not is_student:
            print("Only students can continue.")
            exit()

        self.data = {}
        self.data["name"] = input("Enter your name: ")
        self.data["surname"] = input("Enter your surname: ")
       
        gender = input("Enter your gender (M/F/Other): ").strip().lower()
        if gender == "m":
            self.data["gender"]="Male"

        elif gender =="f":
            self.data["gender"]="Female"
        else:
            self.data["gender"]="Other"
        
        self.data["weight"] = float(input("Enter your weight (kg): "))
        self.data["height"] = float(input("Enter your height (meters): "))

        current_year = datetime.now().year
        while True:
            try:
                birth_year = int(input("Enter your birth year: "))
                if 1900 <= birth_year <= current_year:
                    break
                print("Enter a valid birth year.")
            except:
                print("Invalid value. Try again.")
        self.data["age"] = current_year - birth_year

        self.data["phone"] = input("Enter your phone number: ")
        self.data["department"] = input("Enter your department: ")
        self.data["level"] = int(input("Enter your school level (1-4): "))
        self.data["id"] = input("Enter your student ID: ")
        self.data["scholarship"] = ask_yes_no("Are you a scholarship holder ?")
        self.data["emergency_name"] = str(input("Emergency contact full name: "))
        self.data["emergency_phone"] = input("Emergency phone number: ")

    def display_card(self):
        print("----------------------")
        print("Here is your student card ")
        print("----------------------")
        for key, value in self.data.items():
            print(f"{key.capitalize():17} : {value}")

        year_remain = 4 - self.data["level"]
        graduation_year = datetime.now().year + year_remain
        print(f"You are in year {self.data['level']}")
        print(f"You will graduate in {graduation_year}")
        print("======================")
        print("END OF THE STUDENT CARD")
        print("======================")

# ============================
if __name__ == "__main__":
    student = Student()
    student.display_card()
