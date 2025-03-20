import os


def list_files_in_folder(folder_path):
    try:
        file_list = []  # Initialize an empty list to store file names

        # Get all file names in the folder
        file_names = os.listdir(folder_path)
        print(file_names)

        # Append each file name to the list
        for file in file_names:
            if os.path.isfile(os.path.join(folder_path, file)):  # Ensure it's a file
                file_list.append(file)

        # Print the list of file names
        print(file_list)
    except FileNotFoundError:
        print(f"The folder '{folder_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the folder '{folder_path}'.")


# Specify the folder path here
folder_path = (
    "./"  # Use '.' for the current folder, or provide an absolute/relative path
)

list_files_in_folder(folder_path)
