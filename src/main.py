import os
import shutil

from block_to_html import block_node_to_html_node

def path_exists(path: str) -> bool:
    pass

def list_files_structure(source: str) -> None:
    # This should recursively show the files only
    current_dir = os.listdir(source)
    for entry in current_dir:
        path = os.path.join(source, entry)
        if os.path.isfile(path):
            print(f"found file {entry} in path {source}")
        else:
            list_files_structure(path)
    return

def copy_file_structure(source: str, destination: str) -> None:
    current_dir = os.listdir(source)
    for entry in current_dir:
        shutil.copy(source, destination)

def check_and_clean(destination: str) -> None:
    # this will check if the destination path exists
    # if not it will create it
    # if yes, it will delete the contents
    if os.path.exists(destination):
        print("Path exists -> path will be cleaned up")
        # this actually removes the directory too
        shutil.rmtree(destination)
        
    else:
        print("Path does not exist -> path will be created")
        os.mkdir(destination, mode=0o755)


def main():
    working_dir = os.getcwd()
    static_dir = os.path.join(working_dir, 'static')
    public_dir = os.path.join(working_dir, 'public')
    print(f"The current working directory is {working_dir}\n")
    list_files_structure(static_dir)

    if not os.path.exists(public_dir):
        os.mkdir(public_dir, mode=0o755)
    copy_file_structure(static_dir, public_dir)

    check_and_clean(public_dir)

if __name__ == "__main__":
    main()

