# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
from functions.write_file import write_file


def main():
    working_dir = "calculator"
    print(write_file(working_dir, "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file("calculator", "pkg2/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))



main()