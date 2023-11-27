
# Define dictionaries with course information
room_numbers = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}

instructors = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

meeting_times = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

# Get user input for course number
user_input = input("Enter a course number: ")

# Display information for the entered course number
try:
    room_number = room_numbers[user_input]
    instructor = instructors[user_input]
    meeting_time = meeting_times[user_input]

    print(f"Course Number: {user_input}")
    print(f"Room Number: {room_number}")
    print(f"Instructor: {instructor}")
    print(f"Meeting Time: {meeting_time}")

except KeyError:
    print("Course not found. Please enter a valid course number.")
