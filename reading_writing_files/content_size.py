import os

#prints the total content of an entire folder on your local PC

def get_folder_size(path):
    dir_list = os.listdir(path)
    total_size = 0

    for filename in dir_list:
        file_path = os.path.join(path, filename)
        total_size += os.path.getsize(file_path)

    return total_size

def main():
    path = '/Users/emmywonder/videos' 
    print(get_folder_size(path))

main()

