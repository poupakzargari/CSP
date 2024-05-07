from constraint import Problem, AllDifferentConstraint

def assign_tasks():
    # Create a CSP problem
    problem = Problem()

    # Define task variables
    tasks = ['Task1', 'Task2', 'Task3', 'Task4']

    # Define person variables
    persons = ['PersonA', 'PersonB', 'PersonC']

    # Define task start and end times
    task_times = {
        'Task1': (1, 3),
        'Task2': (2, 4),
        'Task3': (3, 5),
        'Task4': (1, 6),
    }

    # Define resource requirements for each task
    task_resources = {
        'Task1': 2,
        'Task2': 1,
        'Task3': 3,
        'Task4': 2,
    }

    # Define task priorities
    task_priorities = {
        'Task1': 2,
        'Task2': 3,
        'Task3': 1,
        'Task4': 2,
    }

    # Add variables to the problem
    problem.addVariables(tasks, persons)

    # Add constraints
    for task in tasks:
        problem.addConstraint(AllDifferentConstraint(), [task])

    # Add timing constraints
    for task in tasks:
        start_time, end_time = task_times[task]
        problem.addConstraint(lambda person, st=start_time, et=end_time: st <= person <= et, (task,))

    # Add resource constraints
    for person in persons:
        problem.addConstraint(lambda *tasks_assigned, p=person: sum(task_resources[t] for t in tasks_assigned) <= 5, tasks)

    # Add priority constraints
    for task in tasks:
        problem.addConstraint(lambda person, priority=task_priorities[task]: priority * (tasks.index(task) + 1) == person, (task,))

    # Solve the problem
    solutions = problem.getSolutions()

    # Print the solutions
    for solution in solutions:
        print(solution)

# Call the function to solve the problem
assign_tasks()
