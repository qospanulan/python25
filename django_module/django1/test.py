import sys


arguments = sys.argv
available_commands = ["runserver", "startproject"]

command = arguments[1]
# command = input("Command is: ")


if command == "runserver":
    print("Congratulations!")
else:
    commands_as_str = '\n'.join(available_commands)
    print(f"Command Not Found!\n\nYou can try commands:\n{commands_as_str}")
