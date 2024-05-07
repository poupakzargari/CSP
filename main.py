# from constraint import Problem
#
#
# class Task:
#     def __init__(self, name, start_time, end_time, resources, priority, dependencies=[]):
#         self.name = name
#         self.start_time = start_time
#         self.end_time = end_time
#         self.resources = resources
#         self.priority = priority
#         self.dependencies = dependencies if dependencies is not None else []
#
#
# def create_csp(tasks):
#     problem = Problem()
#
#     task_variables = {}
#     for task in tasks:
#         variable_name = f"{task.name}_assignee"
#         problem.addVariable(variable_name, [person["name"] for person in people])
#         task_variables[task.name] = variable_name
#
#     for task in tasks:
#         for dependency in task.dependencies:
#             problem.addConstraint(lambda x, y: x != y, (task_variables[task.name], task_variables[dependency.name]))
#
#     # Add resource constraints
#     for task in tasks:
#         for resource, required_amount in task.resources.items():
#             resource_constraint = lambda *values, task=task, resource=resource, required_amount=required_amount: \
#                 sum(1 for person in values if
#                     person in [p["name"] for p in people] and people[[p["name"] for p in people].index(person)][
#                         "resources"].get(resource, 0) > 0) >= required_amount
#
#             problem.addConstraint(resource_constraint)
#
#     for i in range(len(tasks) - 1):
#         problem.addConstraint(lambda x, y: x >= y, (task_variables[tasks[i].name], task_variables[tasks[i + 1].name]))
#
#     return problem
#
#
# def solve_csp(problem):
#     solutions = problem.getSolutions()
#
#     if solutions:
#         for solution in solutions:
#             print("Solution:")
#             for task, assignees in solution.items():
#                 print(f"- {task}_assignee assigned to {', '.join(assignees)}")
#             print("\n")
#     else:
#         print("No solution found.")
#
#
#
#
# tasks = [
#     Task("Pre-delivery of the report", "January 1", "January 15", {"researcher": 1, "author": 1}, "High"),
#     Task("Application programming", "January 5", "January 25", {"programmer": 1, "user_interface_designer": 1}, "Medium"),
#     Task("Testing and troubleshooting", "January 20", "February 1", {"tester": 1}, "Low"),
# ]
#
#
# tasks[1].dependencies = [tasks[0]]
# tasks[2].dependencies = [tasks[1]]
#
# people = [
#     {"name": "Person 1", "resources": {"author": 1}},
#     {"name": "Person 2", "resources": {"researcher": 1}},
#     {"name": "Person 3", "resources": {"tester": 1}},
#     {"name": "Person 4", "resources": {"user_interface_designer": 1}},
#     {"name": "Person 5", "resources": {"programmer": 1}},
#
# ]
#
# # Create and solve CSP
# problem = create_csp(tasks)
# solve_csp(problem)
#

from constraint import Problem


class Task:
    def __init__(self, name, resources):
        self.name = name
        self.resources = resources


def create_csp(tasks, people):
    problem = Problem()

    task_variables = {}
    for task in tasks:
        variable_name = f"{task.name}_assignee"
        problem.addVariable(variable_name, [person["name"] for person in people])
        task_variables[task.name] = variable_name

    for i in range(len(tasks) - 1):
        problem.addConstraint(lambda x, y: x != y, (task_variables[tasks[i].name], task_variables[tasks[i + 1].name]))

    for task in tasks:
        problem.addConstraint(lambda x, task=task, task_variable=task_variables[task.name]: x == task_variable)

    for task in tasks:
        problem.addConstraint(lambda x, task=task: people[[p["name"] for p in people].index(x)]["resources"] == task.resources,
                              (task_variables[task.name],))

    return problem


def solve_csp(problem):
    solutions = problem.getSolutions()

    if solutions:
        for solution in solutions:
            print("Solution:")
            for task, assignee in solution.items():
                print(f"- {task}_assignee assigned to {assignee}")
            print("\n")
    else:
        print("No solution found.")


tasks = [
    Task("Pre-delivery of the report", {"researcher": 1, "author": 1}),
    Task("Application programming", {"programmer": 1, "user_interface_designer": 1}),
    Task("Testing and troubleshooting", {"tester": 1}),
]

people = [
    {"name": "Person 1", "resources": {"author": 1, "researcher": 1}},
    {"name": "Person 2", "resources": {"tester": 1}},
    {"name": "Person 3", "resources": {"user_interface_designer": 1, "programmer": 1}},
]

# Create and solve CSP
problem = create_csp(tasks, people)
solve_csp(problem)

