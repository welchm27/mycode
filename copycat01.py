#!/usr/bin/env python3

def main():
    import shutil
    import os

    # start the program in the home directory
    os.chdir("/home/student/mycode/")

    # copy the file from source to destination
    # shutil.copy(source, destination)
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # copytree will copy an entire directory instead
    shutil.copytree("5g_research/", "5g_research_backup/")




if __name__ == "__main__":
    main()
