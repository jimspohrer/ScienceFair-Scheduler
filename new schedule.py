# Global Variables
NUM_JUDGES = 5 # Number of judges
NUM_PROJECTS = 32 # Number of science fair projects to be judged
NUM_SLOTS = 44  # Number of time slots (11 Hours x 15 minute)

AVAILABILITY_CONSTRAINTS = {
    'Projects 1-9': [1, 2, 3],  # Not available for hours 1, 2, 3
    'Projects 10-19': [4, 5],    # Not available for hours 4, 5
    'Projects 20-29': [6, 7, 8],  # Not available for hours 6, 7, 8
    'Projects 30-32': [1, 2, 3, 9, 10, 11]  # Not available for hours 1, 2, 3, 9, 10, 11
}

global schedule
global available_projects

# Function to check project availability
def is_project_available(project, time_slot):
    hour = int(time_slot/4) + 1
    if 1 <= project <= 9 and hour in AVAILABILITY_CONSTRAINTS['Projects 1-9']:
        return False
    if 10 <= project <= 19 and hour in AVAILABILITY_CONSTRAINTS['Projects 10-19']:
        return False
    if 20 <= project <= 29 and hour in AVAILABILITY_CONSTRAINTS['Projects 20-29']:
        return False
    if 30 <= project <= 32 and hour in AVAILABILITY_CONSTRAINTS['Projects 30-32']:
        return False
    return True

# Function to generate the schedule
def generate_schedule():
    schedule = {f'Judge {chr(65 + i)}': [] for i in range(NUM_JUDGES)}  # A, B, C, D, E
    

    # Create a dictionary to look up if a project is available during a time slot
    available_projects = {}
    for slot in range(1, NUM_SLOTS + 1):
        slot_id = "Slot " + str(slot)
        if slot_id not in available_projects:
            available_projects[slot_id] = []
        for project in range(1, NUM_PROJECTS + 1):
            if is_project_available(project, slot):
                available_projects[slot_id] = available_projects[slot_id] + [project]
                
    
    # Iterate through each judge and assign their schedule (slot, project)
    for judge in schedule.keys():
        for slot in range(1, NUM_SLOTS + 1):
            judge_schedule = schedule[judge]
            slot_id = "Slot " + str(slot)
            available = available_projects[slot_id]
            sched = False
            for project in available:
                if (sched == False) and (project not in judge_schedule):
                    schedule[judge] = schedule[judge] + [project]
                    sched = project
            if sched == False:
                # print("Skip Error - Free time - project 0:",judge,slot)
                schedule[judge] = schedule[judge] + [0]
            else:
                i = available.index(sched)
                available_projects[slot_id] = available[:i]+available[i+1:]
                    
    
    return schedule

# Function to generate HTML table
def generate_html(schedule):
    html_content = """
    <html>
    <head>
        <title>Science Fair Schedule</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: center;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h2>Science Fair Schedule</h2>
        <table>
            <tr>
                <th>Time Slot</th>
                <th>Judge A</th>
                <th>Judge B</th>
                <th>Judge C</th>
                <th>Judge D</th>
                <th>Judge E</th>
            </tr>
    """
    
    # Create a time slot for each hour
    for slot in range(1, NUM_SLOTS + 1):
        row = f"<tr><td>Slot {slot}</td>"
        for judge in schedule.keys():
            # Find the project assigned to the judge=
            project_assigned = schedule[judge][slot-1]
            row += f"<td>Project {project_assigned if project_assigned else 'Break'}</td>"
        row += "</tr>"
        html_content += row
    
    html_content += """
        </table>
    </body>
    </html>
    """
    
    return html_content

# Function to save HTML to a file
def save_html_to_file(html_content, filename='science_fair_schedule.html'):
    with open(filename, 'w') as file:
        file.write(html_content)

# Main execution
if __name__ == "__main__":
    schedule = generate_schedule()
    html_content = generate_html(schedule)
    save_html_to_file(html_content)
    print("Schedule has been saved to 'science_fair_schedule.html'.")

