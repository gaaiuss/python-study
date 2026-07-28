"""
Task list that allows the user to add itens and commands on a task list.
If it is a command it executes the action else it add the item on the list.
The user is allowed to refactor or clear the last action done.
"""


def pretty_list(str_list: list[str]) -> None:
    print(*str_list, sep="\n")


def is_list_empty(str_list: list[str]) -> bool:
    return len(str_list) == 0


commands = "list", "redo", "undo"
task_list: list[str] = []
recicle_bin: list[str] = []

while True:
    print()
    print("Commands: ", end="")
    print(*commands, sep=", ")
    print()
    user_input = input("Type a task or command: ")
    print()

    if user_input not in commands:
        task_list.append(user_input)
        print("TASKS:")
        pretty_list(task_list)

    elif user_input == "list":
        if is_list_empty(task_list):
            print("Task list empty.")
            continue

        print("TASKS:")
        pretty_list(task_list)

    elif user_input == "undo":
        if is_list_empty(task_list):
            print("Nothing to undo.")
            continue

        recicle_bin.append(task_list.pop())
        pretty_list(task_list)

    else:
        if is_list_empty(recicle_bin):
            print("Nothing to redo.")
            continue

        task_list.append(recicle_bin.pop())
        print("TASKS:")
        pretty_list(task_list)
