import os
import shutil


def empty_directory(folder_name):
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




def main():
    source = os.getcwd() + "/static"
    destination = os.getcwd() + "/public"

    empty_directory("public")
    copy_directory(source, destination)





if __name__ == "__main__":
    main()