from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    working_directory = "calculator"
    #message = write_file(working_directory, "pkg/wwlorem.txt", "Hello my name is mohamed")
    #print(message)
    #message = write_file(working_directory, "../temp.txt", "Hello")
    #print(message)
    #message = write_file(working_directory, "temp.txt", "Hello")
    #print(message)
    #message = write_file(working_directory, "pkg2/temp.txt", "Hello")
    #print(message)
    print(run_python_file(working_directory, "main.py"))
    print(run_python_file(working_directory, "tests.py"))
    print(run_python_file(working_directory, "../main.py"))
    print(run_python_file(working_directory, "noneexistent.py"))
main()