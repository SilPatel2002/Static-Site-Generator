import os
import sys
import shutil
from markdown_to_html_node import markdown_to_html_node
from conversion import extract_markdown_header


def empty_directory(folder_name):
    os.makedirs(folder_name, exist_ok=True)
    path = os.getcwd() + "/" + folder_name
    shutil.rmtree(path)
    os.mkdir(folder_name)


def copy_directory(source, destination):    
    source_list =  os.listdir(source)

    if not source_list:
        return

    for file in source_list:
        new_source = source + "/" + file
        new_destination = destination + "/" + file

        if os.path.isfile(new_source):
            shutil.copy(new_source, new_destination)

        else:
            os.mkdir(new_destination)
            copy_directory(new_source, new_destination)


def generate_page(basepath: str, from_path: str, template_path: str, dest_path: str) -> None:
    
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as file:
        content = file.read()

    with open(template_path) as file:
        template = file.read()

    node = markdown_to_html_node(content)
    html = node.to_html()
    header = extract_markdown_header(content)

    template = template.replace("{{ Title }}", header)
    template = template.replace("{{ Content }}", html)
    template = template.replace("href=\"/", f"href=\"{basepath}")
    template = template.replace("src=\"/", f"src=\"{basepath}")


    directories_needed = os.path.dirname(dest_path)
    os.makedirs(directories_needed, exist_ok=True)


    with open(dest_path, "w") as file:
        file.write(template)

    return


def generate_pages_recursive(basepath: str, dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    source_list = os.listdir(dir_path_content)

    if not source_list:
        return
    
    for file in source_list:
        new_source = dir_path_content + "/" + file
        new_destination = dest_dir_path + "/" + file

        if os.path.isfile(new_source):
            if new_source.endswith(".md"):
                base, ext = os.path.splitext(new_destination)
                new_destination = base + ".html"
                generate_page(basepath, new_source, template_path, new_destination)

        else:
            os.makedirs(new_destination, exist_ok=True)
            generate_pages_recursive(basepath, new_source, template_path, new_destination)




def main():

    if len(sys.argv) <= 1:
        basepath = "/"
        
    else:
        basepath = sys.argv[1]


    empty_directory("docs")
    copy_directory("static", "docs")
    
    generate_pages_recursive(basepath, "content", "template.html", "docs")

 

    





if __name__ == "__main__":
    main()