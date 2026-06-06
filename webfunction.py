from pathlib import Path

FilePath = Path(__file__).parent/"todo.txt"
#FilePath = "todo.txt"
def get_todos(filepath=FilePath):
    with open(filepath, 'r') as file:
        text_input = file.readlines()
    return text_input

def write_todos(todos, filepath=FilePath):
    with open(filepath, 'w') as file:
        file.writelines(todos)


if __name__ == '__main__':
    print(get_todos())