def clear_file(file_path):

    with open(file_path, 'w') as f:
        pass
    print(f"All data in '{file_path}' has been deleted.")