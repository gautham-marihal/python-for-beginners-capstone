import random
import os
from getpass import getpass

def pause():
    input("\nPress Enter to continue...")

#College Assistance
def college_assistance():
    while True:
        os.system('cls')
        print("\nHow can I assist you with your college needs?")
        print("1. Study Tips")
        print("2. Time Management Advice")
        print("3. Educational Motivation")
        print("4. Course Recommendations")
        print("5. Attendance Tracking")
        print("6. Number of classes to attend to reach 75% Attendance")
        print("7. Percentage Calculator")
        print("8. Study Planner")
        print("9. Converter")
        print("10. Back to Main Menu")

        choice = input("Enter your choice (1-10): ").lower()

        if choice == '1' or choice == 'study tips':
            print("\nAnswer a few questions to get the best study tip for you!")
            problem = input("What is your biggest study problem?\n(a) I can't stay consistent\n(b) I get distracted easily\n(c) I feel burned out\n(d) I forget what I study\nAnswer: ").lower()
            if problem == 'a' or problem == "i can't stay consistent":
                print("Tip: Create a study schedule and stick to it!")
            elif problem == 'b' or problem == "i get distracted easily":
                print("Tip: Find a quiet study space with no distractions!")
            elif problem == 'c' or problem == "i feel burned out":
                print("Tip: Take regular breaks using the Pomodoro technique!")
            elif problem == 'd' or problem == "i forget what I study":
                print("Tip: Use flashcards to revise and retain information!")
            else:
                print("Invalid choice. Please try again.")
            pause()

        elif choice == '2' or choice == 'time management advice':
            print("\nAnswer a few questions to get the best time management advice!")
            problem = input("What is your biggest time management problem?\n(a) I don't know what to do first\n(b) I keep delaying tasks\n(c) I set unrealistic goals\n(d) I lose track of tasks\nAnswer: ").lower()
            if problem == 'a' or problem == "i don't know what to do first":
                print("Advice: Prioritize your tasks using the Eisenhower Matrix!")
            elif problem == 'b' or problem == "i keep delaying tasks":
                print("Advice: Avoid procrastination by breaking tasks into smaller steps!")
            elif problem == 'c' or problem == "i set unrealistic goals":
                print("Advice: Set realistic and achievable goals using the SMART method!")
            elif problem == 'd' or problem == "i lose track of tasks":
                print("Advice: Use a planner or to-do list to track your tasks!")
            else:
                print("Invalid choice. Please try again.")
            pause()

        elif choice == '3' or choice == 'educational motivation':
            motivation = [
                "Believe in yourself",
                "Set clear goals",
                "Stay focused",
                "Learn from failures",
                "The illiterate of the future will not be the person who cannot read. It will be the person who does not know how to learn.",
                "The roots of education are bitter, but the fruit is sweet."
            ]
            mot = random.choice(motivation)
            print(f"Here's some educational motivation: {mot}")
            pause()

        elif choice == '4' or choice == 'course recommendations':
            print("\nAnswer a few questions to get your course recommendation!")
            interest = input("What are you interested in?\n(a) Computers\n(b) Business\n(c) Human Behavior\n(d) Building Things\n(e) Living Organisms\nAnswer: ").lower()
            if interest == 'a' or interest == "computers":
                print("I recommend you to consider studying Computer Science!")
            elif interest == 'b' or interest == "business":
                print("I recommend you to consider studying Business!")
            elif interest == 'c' or interest == "human behavior":
                print("I recommend you to consider studying Psychology!")
            elif interest == 'd' or interest == "building things":
                print("I recommend you to consider studying Engineering!")
            elif interest == 'e' or interest == "living organisms":
                print("I recommend you to consider studying Biology!")
            else:
                print("Invalid choice. Please try again.")
            pause()

        elif choice == '5' or choice == 'attendance tracking':
            number_of_classes = int(input("Enter the total number of classes: "))
            number_of_classes_attended = int(input("Enter the number of classes you have attended: "))
            if number_of_classes_attended == 0:
                print("Total number of classes cannot be zero.")
            else:
                total_attendance = (number_of_classes_attended / number_of_classes) * 100
                print(f"Your attendance percentage is: {total_attendance:.2f}%")
            pause()

        elif choice == '6' or choice == 'number of classes to attend to reach 75% attendance':
            total_classes = int(input("Enter the total number of classes: "))
            attended_classes = int(input("Enter the number of classes you have attended: "))
            classes_needed = ((0.75 * total_classes) - attended_classes) / 0.25
            if classes_needed <= 0:
                print("You have already reached 75% Attendance. Keep it up!")
            else:
                print(f"You need to attend {classes_needed:.1f} classes to reach 75% attendance.")
            pause()

        elif choice == '7' or choice == 'percentage calculator':
            total_marks = float(input("Enter the total marks: "))
            obtained_marks = float(input("Enter the marks you obtained: "))
            percentage = (obtained_marks / total_marks) * 100
            print(f"Your percentage is: {percentage:.2f}%")
            pause()

        elif choice == '8' or choice == 'study planner':
            print("Here's your study planner!")
            number_of_subjects = int(input("Enter the number of subjects you have: "))
            number_of_days_for_exam = int(input("Enter the number of days left for the exam: "))
            study_hours_per_day = int(input("Enter the number of hours you can study per day: "))
            total_study_hours = number_of_days_for_exam * study_hours_per_day
            hours_per_subject = total_study_hours / number_of_subjects
            print(f"Total study hours: {total_study_hours}")
            print(f"Hours per subject: {hours_per_subject:.2f}")
            pause()

        elif choice == '9' or choice == 'converter':
            conv = input("Choose the converter you want to use:\n1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit\n3. cm to m\n4. m to cm\n5. kg to pounds\n6. pounds to kg\n7. Return to Main Menu\nChoose the converter (1-7): ").lower()

            if conv == '1' or conv == 'fahrenheit to celsius':
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                C = (fahrenheit - 32) * 0.55
                print(f"Fahrenheit in Celsius is {C:.2f}")
            
            elif conv == '2' or conv == 'celsius to fahrenheit':
                celsius = float(input("Enter temperature in Celsius: "))
                F = (celsius * 1.8) + 32
                print(f"Celcius in Fahrenheit is {F:.2f}")
            
            elif conv == '3' or conv == 'cm to m':
                cm = float(input("Enter distance in cm: "))
                m = cm/100
                print(f"cm in m is {m:.2f} m")

            elif conv == '4' or conv == 'm to cm':
                m = float(input("Enter distance in m: "))
                cm = m*100
                print(f"m in cm is {cm:.2f} cm")
            
            elif conv == '5' or conv == 'kg to pounds':
                kgs = float(input("Enter weight in kg: "))
                pounds = kgs * 2.20462
                print(f"kg in pounds is {pounds:.2f} lbs")

            elif conv == '6' or conv == 'pounds to kgs':
                pounds = float(input("Enter weight in pounds: "))
                kgs = pounds / 2.20462
                print(f"Pounds in kgs is {kgs:.2f} kg")
            

            elif conv == '7' or conv == 'return to main menu':
                print("Returning to Main Menu")
                return 
            
            else:
                print("Invalid choice ")
            pause()

        elif choice == '10' or choice == 'back to main menu':
            print("Returning to Main Menu...")
            return

        else:
            print("Invalid choice. Please try again.")
            pause()


# FunZone
def funzone():
    while True:
        os.system('cls')
        games = input("\nWelcome to the Fun Zone! What game would you like to play?\n1. RPS (rock, paper, scissors)\n2. Guess the Number\n3. Back to Main Menu\nEnter your choice: ").lower()

        if games == 'rps' or games == '1' or games == 'rock paper scissors':
            player_score = 0
            computer_score = 0

            for _ in range(5):
                player = input('Enter your choice (rock/paper/scissors): ').lower()
                choices = ['rock', 'paper', 'scissors']
                computer = random.choice(choices)
                print(f"Computer chose: {computer}")

                if player == computer:
                    print('Match tied')
                elif ((player == 'rock' and computer == 'scissors') or (player == 'r' and computer == 'scissors')) \
                        or ((player == 'paper' and computer == 'rock') or (player == 'p' and computer == 'rock')) \
                        or ((player == 'scissors' and computer == 'paper') or (player == 's' and computer == 'paper')):
                    print('Player wins')
                    player_score += 1
                else:
                    print('Computer wins')
                    computer_score += 1

            print(f"\nFinal Score - Player: {player_score} | Computer: {computer_score}")
            if player_score > computer_score:
                print("Player wins the game!")
            elif computer_score > player_score:
                print("Computer wins the game!")
            else:
                print("It's a tie!")
            pause()

        elif games == 'guess the number' or games == '2':
            secret_num = random.randint(1, 100)
            attempts = 8
            print('Guess a number between 1-100 in 8 attempts')
            guessed_correctly = False

            while attempts > 0:
                guess_number = int(input('Enter your guess: '))

                if secret_num == guess_number:
                    print('You guessed it right!!')
                    guessed_correctly = True
                    break
                elif secret_num < guess_number:
                    print('Guess a lower number')
                else:
                    print('Guess a higher number')

                attempts -= 1
                print(f'You have {attempts} attempts left')

            if not guessed_correctly:
                print(f'You lost the game! The correct number was {secret_num}')
            pause()

        elif games == 'back' or games == '3':
            print("Returning to Main Menu...")
            return

        else:
            print("Invalid choice. Please try again.")
            pause()


# Calories Calculator
def calories_calculator():

    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (cm): "))
        age = int(input("Enter your age: "))
        gender = input("Enter your gender (male/female): ").lower()

        if gender not in ["male", "female"]:
            print("Invalid gender entered!")
            return

    except ValueError:
        print("Please enter valid numeric values.")
        return

    # Load food items from file
    if not os.path.exists("food_items.txt"):
        open("food_items.txt", "w").close()
    food_items = {}
    with open("food_items.txt", "r") as f:
        for line in f:
            name, cal = line.strip().split(":")
            food_items[name] = int(cal)

    # BMR Calculation
    if gender == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    while True:
        os.system('cls')
        print("\n===== HEALTH & FITNESS ASSISTANT =====")
        print("1. Weight Gain")
        print("2. Weight Loss")
        print("3. Maintain Weight")
        print("4. View Food Items with Calories")
        print("5. Water Intake Calculator")
        print("6. BMI Calculator")
        print("7. Add Food Item")
        print("8. Remove Food Item")
        print("9. Back to Main Menu")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            calories_needed = bmr + 300
            print("\nFoods Recommended For Weight Gain:")
            print("1. Eggs : 150 kcal (1 egg)\n2. Milk : 150 kcal (1 glass)\n3. Rice : 200 kcal (1 cup)\n4. Peanut Butter : 190 kcal (1 tbsp)\n5. Bananas : 105 kcal (1 medium)\n6. Paneer : 300 kcal (100g)")
            print(f"\nRecommended Calories: {calories_needed:.2f} kcal/day")
            pause()

        elif choice == "2":
            calories_needed = bmr - 300
            print("\nFoods Recommended For Weight Loss:")
            print("1. Vegetables : 50 kcal (1 cup)\n2. Fruits : 80 kcal (1 medium)\n3. Oats : 150 kcal (1 cup)\n4. Salads : 100 kcal (1 bowl)\n5. Lean Protein : 200 kcal (100g)\n6. Greek Yogurt : 120 kcal (1 cup)")
            print(f"\nRecommended Calories: {calories_needed:.2f} kcal/day")
            pause()

        elif choice == "3":
            print(f"\nRecommended Calories: {bmr:.2f} kcal/day")
            pause()

        elif choice == "4":
            print("\n===== FOOD CALORIES =====")
            for item, calories in food_items.items():
                print(f"{item.title()} : {calories} kcal")
            pause()

        elif choice == "5":
            water_intake = weight * 0.035
            print(f"\nRecommended Water Intake: {water_intake:.2f} liters/day")
            pause()

        elif choice == "6":
            height_m = height / 100
            bmi = weight / (height_m ** 2)
            print(f"\nYour BMI: {bmi:.2f}")
            if bmi < 18.5:
                print("Category: Underweight")
            elif bmi < 25:
                print("Category: Normal Weight")
            elif bmi < 30:
                print("Category: Overweight")
            else:
                print("Category: Obese")
            pause()

        elif choice == "7":
            name = input("Enter food item name: ").lower()
            cal = int(input(f"Enter calories for {name.title()}: "))
            food_items[name] = cal
            with open("food_items.txt", "w") as f:
                for item, calories in food_items.items():
                    f.write(f"{item}:{calories}\n")
            print(f"{name.title()} added successfully!")
            pause()

        elif choice == "8":
            name = input("Enter food item name to remove: ").lower()
            if name in food_items:
                del food_items[name]
                with open("food_items.txt", "w") as f:
                    for item, calories in food_items.items():
                        f.write(f"{item}:{calories}\n")
                print(f"{name.title()} removed successfully!")
            else:
                print(f"{name.title()} not found!")
            pause()

        elif choice == "9":
            print("Exiting Health & Fitness Assistant...")
            return

        else:
            print("Invalid choice! Please try again.")
            pause()


#Mood Detector
def mood_detector():
    happy_words = ["happy", "great", "good", "excited"]
    sad_words = ["sad", "depressed", "upset", "crying"]
    stress_words = ["stressed", "stress", "exam", "pressure", "worried"]
    angry_words = ["angry", "mad", "furious", "annoyed"]

    mood = input("How are you feeling today? ").lower()

    if any(word in mood for word in happy_words):
        print("You seem happy today!")
    elif any(word in mood for word in sad_words):
        print("You seem sad. Tomorrow is a new day.")
    elif any(word in mood for word in stress_words):
        print("You seem stressed. Take a short break and breathe.")
    elif any(word in mood for word in angry_words):
        print("You seem angry. Try to stay calm.")
    else:
        print("I couldn't determine your mood.")
    pause()


# Quiz Area
def quiz_area():
    while True:
        os.system('cls')
        print("\nWelcome to the Quiz Area!")

        options = input(
            "1. General Knowledge\n"
            "2. Science\n"
            "3. Python\n"
            "4. Back to Main Menu\n"
            "Enter your choice (1-4): "
        )

        score = 0

        # GENERAL KNOWLEDGE
        if options == '1':
            print("\n===== GENERAL KNOWLEDGE QUIZ =====")

            answer = input("1. What is the capital of India?\n(a) Mumbai\n(b) Delhi\n(c) Chennai\nAnswer: ").lower()
            if answer == "b" or answer == "delhi":
                score += 1

            answer = input("\n2. How many continents are there?\n(a) 5\n(b) 6\n(c) 7\nAnswer: ").lower()
            if answer == "c" or answer == "7":
                score += 1

            answer = input("\n3. Which planet is known as the Red Planet?\n(a) Mars\n(b) Venus\n(c) Jupiter\nAnswer: ").lower()
            if answer == "a" or answer == "mars":
                score += 1

            answer = input("\n4. Who wrote Romeo and Juliet?\n(a) Charles Dickens\n(b) William Shakespeare\n(c) Jane Austen\nAnswer: ").lower()
            if answer == "b" or answer == "william shakespeare":
                score += 1

            answer = input("\n5. How many days are in a leap year?\n(a) 365\n(b) 366\n(c) 364\nAnswer: ").lower()
            if answer == "b" or answer == "366":
                score += 1

            answer = input("\n6. Which is the largest ocean?\n(a) Atlantic\n(b) Indian\n(c) Pacific\nAnswer: ").lower()
            if answer == "c" or answer == "pacific":
                score += 1

            print(f"\nYour Score: {score}/6")

        # SCIENCE
        elif options == '2':
            print("\n===== SCIENCE QUIZ =====")

            answer = input("1. What is H2O?\n(a) Oxygen\n(b) Water\n(c) Hydrogen\nAnswer: ").lower()
            if answer == "b" or answer == "water":
                score += 1

            answer = input("\n2. Which planet is closest to the Sun?\n(a) Mercury\n(b) Earth\n(c) Mars\nAnswer: ").lower()
            if answer == "a" or answer == "mercury":
                score += 1

            answer = input("\n3. How many bones are in an adult human body?\n(a) 206\n(b) 250\n(c) 180\nAnswer: ").lower()
            if answer == "a" or answer == "206":
                score += 1

            answer = input("\n4. What is the chemical symbol for Gold?\n(a) Go\n(b) Gd\n(c) Au\nAnswer: ").lower()
            if answer == "c" or answer == "au":
                score += 1

            answer = input("\n5. What gas do plants absorb?\n(a) Oxygen\n(b) Carbon Dioxide\n(c) Nitrogen\nAnswer: ").lower()
            if answer == "b" or answer == "carbon dioxide":
                score += 1

            answer = input("\n6. How many chambers does a human heart have?\n(a) 2\n(b) 3\n(c) 4\nAnswer: ").lower()
            if answer == "c" or answer == "4":
                score += 1

            print(f"\nYour Score: {score}/6")

        # PYTHON 
        elif options == '3':
            print("\n===== PYTHON QUIZ =====")

            answer = input("1. Which keyword is used to create a function?\n(a) function\n(b) define\n(c) def\nAnswer: ").lower()
            if answer == "c" or answer == "def":
                score += 1

            answer = input("\n2. Which symbol is used for comments?\n(a) //\n(b) #\n(c) /*\nAnswer: ").lower()
            if answer == "b" or answer == "#":
                score += 1

            answer = input("\n3. What is the output of len('Python')?\n(a) 5\n(b) 6\n(c) 7\nAnswer: ").lower()
            if answer == "b" or answer == "6":
                score += 1

            answer = input("\n4. Which keyword is used for loops?\n(a) loop\n(b) iterate\n(c) for\nAnswer: ").lower()
            if answer == "c" or answer == "for":
                score += 1

            answer = input("\n5. What is the correct file extension for Python?\n(a) .pt\n(b) .py\n(c) .pyt\nAnswer: ").lower()
            if answer == "b" or answer == ".py":
                score += 1

            answer = input("\n6. Which function is used to display output?\n(a) print()\n(b) display()\n(c) show()\nAnswer: ").lower()
            if answer == "a" or answer == "print()":
                score += 1

            print(f"\nYour Score: {score}/6")

        # BACK
        elif options == '4':
            print("Returning to Main Menu...")
            return

        else:
            print("Invalid choice. Please try again.")
            pause()
            continue

        # PERFORMANCE
        if score == 6:
            print("Excellent! Perfect Score!")
        elif score >= 4:
            print("Good Job!")
        elif score >= 2:
            print("Keep Practicing!")
        else:
            print("Better luck next time!")
        pause()


#Viewing Profiles (Admin Use Only)
def profiles():
    if not os.path.exists("password.txt"):
        with open("password.txt", "w") as f:
            f.write("12340")
    with open("password.txt", "r") as f:
        stored_password = f.read().strip()
    password = int(getpass("Enter the password to access profiles: "))
    if password == int(stored_password):
        print("1. Access Profiles\n2. Change Password\n3. Delete Profile\n4. Back to Main Menu\n")
        admin = input("Enter your choice: ")
        if admin == '1' or admin == 'access profile':
            with open("profile.txt", "r") as f:
                profiles = f.read()
                print("\n===== PROFILES =====")
                print(profiles)
            pause()
        elif admin == '2' or admin == 'change password':
           old_pass = int((getpass("Old Password: ")))
           if old_pass == int(stored_password):
               new_pass = int(getpass("enter the new password: "))
               if new_pass == old_pass:
                   print("New password cannot be the same as the old password! Password change failed.")
               else:
                     confirm_new_pass = int(getpass("Confirm New Password: "))
               if new_pass == confirm_new_pass:
                   with open("password.txt", "w") as f:
                       f.write(str(new_pass))
                   print("Password changed successfully!")
               else:
                   print("New passwords do not match! Password change failed.")

        elif admin == '3':
            username = input("Username: ")
            age = input("Age: ")
            mail_id = input("Mail ID: ")

            with open("profile.txt", "r") as f:
                content = f.read()

            profile = f"Name: {username}\nAge: {age}\nMail ID: {mail_id}\n\n"

            if profile not in content:
                print("Profile not found")
            else:
                content = content.replace(profile, "")
                with open("profile.txt", "w") as f:
                    f.write(content)
                print("Profile deleted successfully!!")
            pause()

        elif admin == '4' or admin == 'back to main menu':
            print("Returning to Main Menu...")
            return
        else:
            print("Invalid choice.")
            pause()
    else:
        print("Incorrect password! Access denied.")
        pause()


#To-do List
def to_do_list():
    if not os.path.exists("todolist.txt"):
        open("todolist.txt","w").close()
    while True:
        os.system('cls')
        todo = input("1. View Tasks\n2. Add Tasks\n3. Remove Tasks\n4. Back to Main Menu\nChoose your choice (1-4): ").lower()

        if todo == '1' or todo == 'view tasks':
            with open("todolist.txt","r") as f:
                view = f.read()
                if len(view) > 0:
                    print("------- To Do List -------\n")
                    print(view)
                else:
                    print("No Task Available!!")
            pause()

        elif todo == '2' or todo == 'add tasks':
            task = input("Enter task: ").lower()
            with open("todolist.txt","a") as f:
                f.write(task+"\n")
            print("Task added successfully!!")
            pause()

        elif todo == '3' or todo == 'remove tasks':
            task_remove = input("Enter the task to remove: ").lower()
            with open("todolist.txt","r") as f:
                content = f.read()
            if task_remove not in content:
                print("Task not found")
            else:
                content = content.replace(task_remove+"\n","")
                with open("todolist.txt", "w") as f:
                    f.write(content)
                print("Task deleted successfully!!")
            pause()

        elif todo == '4' or todo == 'back to main menu':
            print("Returning to Main Menu ...")
            return

        else:
            print("Invalid choice. Please try again.")
            pause()


# ----------------- MAIN PROGRAM ------------------ #

print('=' * 60)
print("      Welcome to the UniBot! I am here at your service.")
print('=' * 60)

name = input("Enter Your Username: ")

# Create file if it doesn't exist
if not os.path.exists("profile.txt"):
    open("profile.txt", "w").close()

found = False

with open("profile.txt", "r") as f:
    for line in f:
        if line.strip() == f"Name: {name}":
            found = True
            break

if found:
    while True:
        os.system('cls')
        username = input("Enter username again: ")
        password = getpass("Enter password: ")
        if not os.path.exists("User.txt"):
            open("User.txt","w").close()

        with open("User.txt","r") as f:
            content = f.read()
        if f"Name: {username}\nPassword: {password}\n" in content:
            print(f"Welcome back, {name}!")
            pause()
            break
        else:
            print("Wrong username or password. Try again...")
            pause()

else:
    age = int(input("Enter your age: "))
    mail_id = input("Enter your mail id: ")

    with open("profile.txt", "a") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Age: {age}\n")
        f.write(f"Mail ID: {mail_id}\n\n")

    print("Profile created successfully!")
    with open("User.txt","a") as f:
        pwd = input("Enter password: ")
        f.write(f"Name: {name}\n")
        f.write(f"Password: {pwd}\n\n")

print(f"Welcome, {name}!")

while True:
    os.system('cls')
    mode = input(
        "\nSelect a Mode:\n"
        "1. College Assistance\n"
        "2. Calories Calculator\n"
        "3. Mood Detector\n"
        "4. Quiz Area\n"
        "5. To-do List\n"
        "6. Fun Zone\n"
        "7. Profiles (Admin Use Only)\n"
        "8. Exit\n"
        "Enter your choice (1-8): "
    )

    if mode == '1' or mode == 'college assistance':
        college_assistance()
    elif mode == '2' or mode == 'calories calculator':
        calories_calculator()
    elif mode == '3' or mode == 'mood detector':
        mood_detector()
    elif mode == '4' or mode == 'quiz area':
        quiz_area()
    elif mode == '5' or mode == 'to-do list':
        to_do_list()
    elif mode == '6' or mode == 'fun zone':
        funzone()
    elif mode == '7' or mode == 'profiles':
        profiles()
    elif mode == '8' or mode == 'exit':
        ask = input("Are you sure you want to exit? (yes/no): ").lower()
        if ask == "yes" or ask == 'y':
            print("Exiting UniBot... Have a great day!")
            break
        elif ask == "no" or ask == 'n':
            print("Returning to Main Menu..")
            continue
        else:
            print('Invalid choice. Returning back to Main Menu...')
    else:
        print("Invalid choice. Please try again.")
        pause()
