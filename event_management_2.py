from datetime import datetime, timedelta

# Event class definition
class Event:
    def __init__(self, name, start_time, duration):
        self.name = name
        self.start_time = start_time
        self.duration = duration
        self.end_time = start_time + timedelta(hours=duration)

# Agenda class definition with method to add event
class Agenda:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        for e in self.events:
            # Check if the new event overlaps with any existing event
            if (event.start_time < e.end_time and event.end_time > e.start_time):
                return False
        # Add the event to the agenda if no overlap
        self.events.append(event)
        return True

# Helper function to parse date and time
def parse_time(time_str):
    # Remove timezone part manually (e.g., remove ' PST')
    time_str = time_str.rsplit(' ', 1)[0]
    return datetime.strptime(time_str, '%m-%d-%Y %I:%M %p')

# Main function for Question 1(a) and 1(b)
def main():
    # Create an Agenda object
    agenda = Agenda()

    # ---- Question 1(a) ----
    # Get event details from user
    name1 = input("What is the event about: ")
    start_time1_str = input("When does the event start (e.g., 02-15-2024 10:00 AM): ")
    start_time1 = parse_time(start_time1_str)
    duration1 = float(input("How long is the event (in hours): "))
    
    # Create and add event 1
    event1 = Event(name1, start_time1, duration1)
    if agenda.add_event(event1):
        print(f'"{name1}" added to the agenda.')
    else:
        print(f'Did not add "{name1}" because it overlaps with other events.')

    # ---- Question 1(b) ----
    # Get event details for second event from user
    name2 = input("What is the event about: ")
    start_time2_str = input("When does the event start (e.g., 02-15-2024 10:30 AM): ")
    start_time2 = parse_time(start_time2_str)
    duration2 = float(input("How long is the event (in hours): "))
    
    # Create and add event 2
    event2 = Event(name2, start_time2, duration2)
    if agenda.add_event(event2):
        print(f'"{name2}" added to the agenda.')
    else:
        print(f'Did not add "{name2}" because it overlaps with other events.')

# Run the main program
main()
