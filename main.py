import sys
import utils

print("This is argv:", sys.argv)
command = sys.argv[1]
print(command)
if command == "build":
    print("Build was specified")
# TODO: Do something here... elif command == "new":
    
    print("New page was specified")
# TODO: Do something here... else:
    print("Please specify ’build’ or ’new’")