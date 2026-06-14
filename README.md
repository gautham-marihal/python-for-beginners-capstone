# 🎓 UniBot — Your College Assistant

UniBot is a Python-based command-line assistant designed to help college students with academics, health, entertainment, and productivity — all in one place.

---

## 📌 Features

### 1. 🏫 College Assistance
- Study Tips — personalized based on your problem
- Time Management Advice — tailored to your issue
- Educational Motivation — random motivational quotes
- Course Recommendations — based on your interests
- Attendance Tracking — calculates your attendance percentage
- Classes needed to reach 75% Attendance
- Percentage Calculator — calculates your marks percentage
- Study Planner — plans study hours per subject
- Unit Converter — temperature, distance, weight conversions with 6 conversion types and a return option

### 2. 🥗 Calories Calculator
- BMR Calculation based on age, weight, height, and gender
- Weight Gain / Weight Loss / Maintain Weight recommendations
- BMI Calculator
- Water Intake Calculator
- Food Items Manager — add and remove items from `food_items.txt`

### 3. 😊 Mood Detector
- Detects your mood based on keywords you type
- Responds with appropriate advice

### 4. 📝 Quiz Area
- General Knowledge Quiz — 6 questions
- Science Quiz — 6 questions
- Python Quiz — 6 questions
- Performance rating after each quiz

### 5. ✅ To-Do List
- View, Add, and Remove tasks
- Tasks saved permanently in `todolist.txt`

### 6. 🎮 Fun Zone
- Rock Paper Scissors — 5 rounds with final score
- Guess the Number — 8 attempts to guess a number between 1-100

### 7. 🔐 Profiles (Admin Only)
- View all registered user profiles
- Change admin password
- Delete a user profile

---

## 🗂️ Files Used

| File | Purpose |
|------|---------|
| `unibot.py` | Main program file |
| `profile.txt` | Stores user profiles |
| `User.txt` | Stores usernames and passwords |
| `password.txt` | Stores admin password |
| `food_items.txt` | Stores food items and calories |
| `todolist.txt` | Stores to-do tasks |

---

## 🚀 How to Run

1. Make sure Python 3 is installed on your system
2. Clone or download this repository
3. Open terminal in the project folder
4. Run the following command

```bash
python unibot.py
```

---

## 👤 Login System

- New users can register with username, age, and mail ID
- Returning users must enter their username and password to login
- Passwords are hidden while typing using `getpass`

---

## 🔑 Default Admin Password

```
12340
```

> Admin can change the password from inside the Profiles section

---

## 🛠️ Built With

- Python 3
- Standard Library Modules only: `random`, `os`, `getpass`
- No external libraries required

---

## 📂 Project Structure

```
UniBot/
│
├── unibot.py          # Main program
├── profile.txt        # Auto-created on first run
├── User.txt           # Auto-created on first run
├── password.txt       # Auto-created on first run
├── food_items.txt     # Add your food items here
├── todolist.txt       # Auto-created on first run
└── README.md
```

---

## 👨‍💻 Author

Made with by Gautham A Marihal
