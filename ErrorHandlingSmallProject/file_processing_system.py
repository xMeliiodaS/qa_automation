import file_handler
from file_operations import write_file


def main():
    file_path = input("Enter the file path: ")
    file_mode = input("Enter the file mode: ")
    if file_mode == "w":
        content = input("Enter the file content: ")
        asd = file_handler.file_handler(file_path, file_mode)
        write_file(asd.args[0], content)


if __name__ == "__main__":
    main()
