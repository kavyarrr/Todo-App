FILEPATH = "todos.txt"


def call(filepath=FILEPATH):
    """Read a text file and return the list of
    to-do items. """
    with open(filepath, 'r') as file:
        tlocal = file.readlines()
    return tlocal


def change(tlocal, filepath=FILEPATH):
    """ Write the todo list items onto the file """
    with open(filepath, "w") as file:
        file.writelines(tlocal)


if __name__ == "__main__":
    print("Hello")
    print(call())
