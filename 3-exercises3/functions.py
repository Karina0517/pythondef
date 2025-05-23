# 1. Library Book Tracker
library = {}

def add_book(title, author, pages):
    library[title] = {"author": author, "pages": pages}

def find_book(title):
    return library.get(title, "Book not found.")

def show_books():
    return list(library.keys())

# 2. Student Grade Manager
grades = {}

def add_student(name):
    grades[name] = []

def add_grade(name, grade):
    if name in grades:
        grades[name].append(grade)

def get_average(name):
    if name in grades and grades[name]:
        return sum(grades[name]) / len(grades[name])

# 3. Restaurant Menu Editor
menu = {}

def add_dish(name, price, available):
    menu[name] = {"price": price, "available": available}

def change_availability(name, available):
    if name in menu:
        menu[name]["available"] = available

def total_available_price():
    return sum(d["price"] for d in menu.values() if d["available"])

# 4. Warehouse Box Counter
warehouse = {}

def add_box(name, quantity):
    warehouse[name] = quantity

def update_quantity(name, quantity):
    if name in warehouse:
        warehouse[name] += quantity

def has_enough(name, required):
    return warehouse.get(name, 0) >= required

# 5. Movie Rating System
movies = {}

def add_movie(title):
    movies[title] = []

def rate_movie(title, rating):
    if title in movies:
        movies[title].append(rating)

def average_rating(title):
    if title in movies and movies[title]:
        return sum(movies[title]) / len(movies[title])

# 6. Online Course Tracker
courses = {}

def add_course(title, duration, enrolled):
    courses[title] = {"duration": duration, "enrolled": enrolled}

def update_enrollment(title, enrolled):
    if title in courses:
        courses[title]["enrolled"] = enrolled

def filter_by_hours(min_duration):
    return [title for title, data in courses.items() if data["duration"] >= min_duration]

# 7. To-Do List Organizer
todos = []

def add_task(description, priority):
    todos.append({"description": description, "priority": priority, "status": "pending"})

def complete_task(description):
    for task in todos:
        if task["description"] == description:
            task["status"] = "completed"

def filter_tasks(priority=None, status=None):
    return [t for t in todos if (priority is None or t["priority"] == priority) and (status is None or t["status"] == status)]

# 8. Digital Wallet
wallet = {}

def add_expense(category, amount):
    wallet[category] = wallet.get(category, 0) + amount

def total_spent():
    return sum(wallet.values())

def expense_percentages():
    total = total_spent()
    return {cat: (amt / total) * 100 for cat, amt in wallet.items()} if total else {}

# 9. Pet Adoption Center
pets = []

def add_pet(name, species, age):
    pets.append({"name": name, "species": species, "age": age})

def find_by_species(species):
    return [p for p in pets if p["species"] == species]

def older_than(age):
    return [p for p in pets if p["age"] > age]

# 10. Gym Membership System
members = {}

def register_member(name, plan, status):
    members[name] = {"plan": plan, "status": status}

def change_plan(name, plan):
    if name in members:
        members[name]["plan"] = plan

def unpaid_members():
    return [name for name, data in members.items() if data["status"] == "late"]

