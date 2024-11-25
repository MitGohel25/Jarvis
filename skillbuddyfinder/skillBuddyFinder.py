import json
from datetime import datetime

# Constants
MAX_USERS = 100
MAX_COURSES = 5
MAX_COURSE_NAME_LEN = 50
MAX_NAME_LEN = 50
MAX_BIO_LEN = 200
MAX_MESSAGES = 100
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"
DATA_FILE = "skill_buddy_data.json"

# Data structures
class User:
    def _init_(self, name, password, courses, bio):
        self.name = name
        self.password = password
        self.courses = courses
        self.bio = bio
        self.messages = []
        self.completion_percentage = self.calculate_completion()
        self.endorsements = []

    def calculate_completion(self):
        completed = sum(bool(x) for x in [self.name, self.password, self.courses, self.bio])
        return (completed / 4) * 100

    def add_message(self, message):
        self.messages.append(message)

    def add_endorsement(self, skill, from_user):
        self.endorsements.append({'skill': skill, 'from_user': from_user})


# Global variables
users = []
messages = []

# Utility Functions
def save_data():
    data = {
        "users": [user._dict_ for user in users],
    }
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, default=str)
    print("Data saved successfully.")

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            for user_data in data.get("users", []):
                user = User(user_data["name"], user_data["password"], user_data["courses"], user_data["bio"])
                users.append(user)
            print("Data loaded successfully.")
    except FileNotFoundError:
        print("No data file found. Starting fresh.")

def register_user():
    if len(users) >= MAX_USERS:
        print("Maximum user limit reached.")
        return

    name = input("Enter name: ").strip()
    if any(user.name == name for user in users):
        print("Username already taken.")
        return

    password = input("Enter password: ").strip()
    bio = input("Enter bio: ").strip()

    num_courses = int(input("Enter number of courses (up to 5): ").strip())
    courses = [input(f"Enter course {i + 1}: ").strip() for i in range(num_courses)]

    user = User(name, password, courses, bio)
    users.append(user)
    print("User registered successfully.")

def login():
    name = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    for user in users:
        if user.name == name and user.password == password:
            print(f"Welcome, {name}!")
            user_menu(user)
            return
    print("Invalid username or password.")

# Features added based on your request

# 1. User Profile Completion
def display_profile_completion(user):
    print(f"Profile Completion: {user.calculate_completion()}%")

# 2. Skill Endorsements
def endorse_skill(user):
    skill = input("Enter skill to endorse: ").strip()
    for target_user in users:
        if target_user != user and skill in target_user.courses:
            target_user.add_endorsement(skill, user.name)
            print(f"Endorsed {target_user.name} for skill: {skill}")
            return
    print("No user found with that skill.")

# 6. Discussion Forums
discussion_forums = {}

def post_to_forum(course):
    if course not in discussion_forums:
        discussion_forums[course] = []
    message = input("Enter your forum post: ").strip()
    discussion_forums[course].append((datetime.now(), message))
    print(f"Posted to {course} forum.")

def view_forum(course):
    if course in discussion_forums:
        print(f"--- {course} Forum ---")
        for date, msg in discussion_forums[course]:
            print(f"[{date}] {msg}")
    else:
        print(f"No posts in {course} forum.")

# 7. Progress Tracking
def set_study_goal(user):
    goal = input("Enter your study goal: ").strip()
    print(f"Study goal set: {goal}")

# 8. Personalized Skill Development Plans
def suggest_study_plan(user):
    for course in user.courses:
        print(f"Suggested study plan for {course}:")
        print(f"1. Basics of {course}")
        print(f"2. Intermediate {course}")