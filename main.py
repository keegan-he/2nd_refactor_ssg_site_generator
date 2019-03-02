import sys

print("This is argv:", sys.argv)
command = sys.argv[1]
print(command)
if command == "build":
    print("Build was specified")
# TODO: Do something here... elif command == "new":
    import utils
    utils.build_pages()
    
    print("New page was specified")
# TODO: Do something here... else:
    print("Please specify ’build’ or ’new’")