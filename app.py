import os
import pathspec

def read_gitignore(gitignore_file):
    with open(gitignore_file, 'r') as f:
        gitignore_lines = f.readlines()
    return [line.strip() for line in gitignore_lines]

def get_all_files(root_folder, gitignore_spec):
    file_list = []
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            file_path = os.path.join(root, file)
            if not gitignore_spec.match_file(file_path):
                file_list.append(file_path)
    return file_list

def get_code_from_file(file_path):
    with open(file_path, 'r') as f:
        code = f.read()
    return code

def get_file_language(file_path):
    _, ext = os.path.splitext(file_path)
    if ext == ".js":
        return "JavaScript"
    elif ext == ".py":
        return "Python"
    elif ext == ".cpp":
        return "C++"
    elif ext == ".java":
        return "Java"
    elif ext == ".c":
        return "C"
    # Add more file extensions and languages here
    return None

def write_codes_to_file(output_file, code_data):
    with open(output_file, 'w') as f:
        for file_path, code in code_data.items():
            f.write(f"File: {file_path}\n")
            f.write("Code:\n")
            f.write("-----\n")
            f.write(code)
            f.write("\n-----\n\n")

if __name__ == "__main__":
    print("start the project")
    root_folder = input("Enter the root folder path: ")
    # find gitignore in root folder not using input
    gitignore_file = input("Enter the .gitignore file path: ")
    output_file = 'output.md'

    gitignore_lines = read_gitignore(gitignore_file)
    gitignore_spec = pathspec.PathSpec.from_lines('gitwildmatch', gitignore_lines)
    
    file_list = get_all_files(root_folder, gitignore_spec)

    code_data = {}
    for file_path in file_list:
        language = get_file_language(file_path)
        if language:
            code = get_code_from_file(file_path)
            code_data[file_path] = code

    write_codes_to_file(output_file, code_data)
    print("start the project")

