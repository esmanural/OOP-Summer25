students = [{
 'first_name' = 'Esmanur',
'last_name' = 'Ural',
'index_number' = '34572',
'nationality' = 'Turkey',
'starting_date' = '2024-11-01',
'courses' = ['Computer security', 'Logistics','Ethics']
},
{
 'first_name' = 'Can',
'last_name' = 'Aslan',
'index_number' = 'TR342',
'nationality' = 'Turkey',
'starting_date' = '2024-09-01',
'courses' = ['Computer Science', 'Match','Ethics']
},
{
 'first_name' = 'Baris',
'last_name' = 'Mirza',
'index_number' = 'TR32551',
'nationality' = 'Turkey',
'starting_date' = '2024-01-01',
'courses' = ['English', 'Match','Marketing']
}
]
def add_student():
    """Adds a new student to the list by prompting for input."""
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    index_number = input("Enter student's index number: ")
    nationality = input("Enter student's nationality: ")
    starting_date = input("Enter starting date (YYYY-MM-DD): ")
    courses = input("Enter courses (comma-separated): ").split(',')
    courses = [course.strip() for course in courses]

    students.append({
        'first_name': first_name,
        'last_name': last_name,
        'index_number': index_number,
        'nationality': nationality,
        'starting_date': starting_date,
        'courses': courses
    })
    print(f"Student {first_name} {last_name} added successfully.")

def display_students():
    """Displays all students in the list."""
    print("\nCurrent Students:")
    for student in students:
        print(f"Name: {student['first_name']} {student['last_name']}, Index: {student['index_number']}")
