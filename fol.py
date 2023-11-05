import os
import filecmp

def get_files_in_folder(folder_path):
    files = []
    for root, directories, filenames in os.walk(folder_path):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

def compare_folders(folder1, folder2):
    folder1_files = get_files_in_folder(folder1)
    folder2_files = get_files_in_folder(folder2)

    non_matching_files = []
    for file1 in folder1_files:
        file1_relative_path = os.path.relpath(file1, folder1)
        file2 = os.path.join(folder2, file1_relative_path)
        if file2 not in folder2_files or not filecmp.cmp(file1, file2):
            non_matching_files.append(file1)

    return non_matching_files

# Example usage
folder1_path = 'C:/Users/Saurabh/source/repos/HelloWorld/HelloWorld/bin/Debug/'
folder2_path = 'C:/Users/Saurabh/Videos/Debut/'
matching_files = compare_folders(folder1_path, folder2_path)

print("Not Matching Files:")
for file_path in matching_files:
    print(file_path)