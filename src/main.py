import os
import shutil
import bs4
from bs4 import BeautifulSoup

from block_to_html import markdown_to_html_node, extract_title

# Test function for recursive function to show all files in tree
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
        src_path = os.path.join(source, entry)
        dest_path = os.path.join(destination, entry)
        if os.path.isfile(src_path):
            print(f"Copying file: {entry}")
            print(f"From        : {source}")
            print(f"To          : {destination}\n")
            shutil.copy(src_path, dest_path)
        else:
            create_dir(dest_path)
            copy_file_structure(src_path, dest_path)
    return

def create_dir(new_dir: str) -> None:
    # Helper function to create a new directory with correct mode
    os.mkdir(new_dir, mode=0o755)

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    src_file: str = None 
    tmp_file: str = None
    print(f"Generating page \nfrom : {from_path} \nto   : {dest_path} \nusing: {template_path}\n")

    # Open template.html
    with open(template_path, mode='r') as f:
        tmp_file = f.read()

    # Open index.md 
    with open(from_path, mode='r') as f:
        src_file = f.read()

    # Get title from index.md
    title = extract_title(src_file)

    tmp_file = tmp_file.replace("{{ Title }}", title)
    tmp_file = tmp_file.replace("{{ Content }}", markdown_to_html_node(src_file).to_html())

    pretty_html = BeautifulSoup(tmp_file, "html.parser")
    formatter = bs4.formatter.HTMLFormatter(indent=4)

    with open(dest_path, mode="w") as f:
        f.write(pretty_html.prettify(formatter=formatter))

    # print(tmp_file)
    
def clean_destination_dir(destination: str) -> None:
    # this will check if the destination path exists
    # if not it will create it
    # if yes, it will delete the contents
    if os.path.exists(destination):
        # print("Path exists -> path will be cleaned up\n")
        # this actually removes the directory too
        shutil.rmtree(destination)
    # Maybe remove this one and use os.makedirs() in the generate_page
    create_dir(destination)

def main():
    working_dir = os.getcwd()
    static_dir = os.path.join(working_dir, 'static')
    public_dir = os.path.join(working_dir, 'public')
    from_path = os.path.join(working_dir, 'content/index.md')
    dest_path = os.path.join(working_dir, 'public/index.html')
    temp_path = os.path.join(working_dir, 'template.html')
    # print(f"The current working directory is {working_dir}\n")

    # list_files_structure(static_dir)
    clean_destination_dir(public_dir)
    copy_file_structure(static_dir, public_dir)
    generate_page(from_path, temp_path, dest_path)

    # clean_destination_dir(public_dir)
    # copy_file_structure(static_dir, public_dir)



if __name__ == "__main__":
    main()

