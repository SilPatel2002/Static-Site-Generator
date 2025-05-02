import os
import shutil



def copy_directory(source, destination):
    path = source + "/index.css"
    shutil.rmtree(destination)
    return os.path.isfile(path)




def main():
    source = os.getcwd() + "/static"
    destination = os.getcwd() + "/public"
    print(copy_directory(source, destination))



main()