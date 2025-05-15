import random
from datetime import datetime, timedelta


students = ["Ashok", "Roshan","Tenzing","Kiron", "Seema"]

start_date = datetime(2025, 5, 12)

days_between = len(students)

presentation_dates = [
    
 ]
current_date = start_date
while len(presentation_dates)<days_between:
    if current_date.weekday()<5:
        presentation_dates.append(current_date)
        current_date += timedelta(days=1)

random.shuffle(presentation_dates)
assignments = dict(zip(students,presentation_dates))

for student,date in assignments.items():
    print(f"{student} presents on {date.strftime('%A, %B, %d, %y')}")


