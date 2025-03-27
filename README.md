# ScienceFair-Scheduler
This is a simple program to generate a schedule for judges of projects at a science fair

The basics are
number of judges
number of projects to judge
avaiability constaints on projects
number of 15 minute time slots for judging
only 1 judge per project at a time
each judge reviews every project
OK for judge to have a break, if no new project to judge available at a specific time slot.

Google Gemini helped create the code - which almost worked.
change 1: instead of 11 hours, use 44 slots of fifteen minutes each
change 2: convert constraints to available_projects dictionary
change 3: be sure to remove projects that have already been judged
change 4: Project N/A -> Project Break
