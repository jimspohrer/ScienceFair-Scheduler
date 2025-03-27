# Global Variables
NUM_JUDGES = 5
NUM_PROJECTS = 32
FAIR_DURATION_HOURS = 11
EVAL_TIME_MINUTES = 10  # Evaluation time per project (can be adjusted, but not less than 5)
AVAILABILITY_CONSTRAINTS = {
    'Projects 1-9': [1, 2, 3],  # Not available for hours 1, 2, 3
    'Projects 10-19': [4, 5],    # Not available for hours 4, 5
    'Projects 20-29': [6, 7, 8],  # Not available for hours 6, 7, 8
    'Projects 30-32': [1, 2, 3, 9, 10, 11]  # Not available for hours 1, 2, 3, 9, 10, 11
}

# Function to check project availability
def is_project_available(project, hour):
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
    project_order = list(range(1, NUM_PROJECTS + 1))
    
    # Iterate through each hour of the fair
    for hour in range(1, FAIR_DURATION_HOURS + 1):
        for project in project_order:
            if is_project_available(project, hour):
                for judge in schedule.keys():
                    # Assign project to judge for the current hour
                    schedule[judge].append((hour, project))
    
    return schedule

# Function to print the schedule
def print_schedule(schedule):
    for judge, visits in schedule.items():
        print(f"\n{judge} Schedule:")
        for hour, project in visits:
            print(f"  Hour {hour}: Project {project}")

# Main execution
if __name__ == "__main__":
    schedule = generate_schedule()
    print_schedule(schedule)
