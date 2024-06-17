import os
import sys

def print_file_contents(folder_path):
    # Iterate through the files in the specified folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        # Check if the current item is a file
        if os.path.isfile(file_path):
            try:
                # Open the file in read mode
                with open(file_path, 'r') as file:
                    # Read the file content
                    content = file.read()
                    
                    # Print the file path and content
                    print(f"file: {file_path}")
                    print(content + "\n")
            except IOError as e:
                print(f"Error reading file: {file_path}")
                print(f"Error details: {str(e)}\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
    else:
        folder_path = input("Enter the folder path: ")
    
    print_file_contents(folder_path)