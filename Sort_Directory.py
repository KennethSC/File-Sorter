import shutil
import os

# Sorts a user inputed folder by grouping
# each file into a folder based off their
# extension, EX: all .pdf files are moved 
# into a file called pdf
def sort_directory(dir):

    if not os.path.isdir(dir):
        print("This directory does not exist.")

    for root, dirs, files in os.walk(dir):
        
        # Loops through all the files in that folder
        for file in files:

            # Gets there extension type and file name
            extension = os.path.splitext(file)[1]
            file_name = os.path.splitext(file)[0]

            # if the file has an extension, then
            # it moves it to the created folder with
            # all the files that have the same extension
            if extension != "":

                dir_name = extension.replace('.','')

                # Creates a folder with the extension name if not already made
                if not os.path.isdir(os.path.join(dir, dir_name)):
                    os.mkdir(os.path.join(dir, dir_name))

                source = dir + "/" + str(file)
                destination = dir + "/" + str(dir_name)

                shutil.move(source, destination)

            # If file has no extesnion, then
            # it gets put in a file called 'other'
            elif extension == "":

                dir_name = "other"

                # If a folder called 'other' is not in that 
                # directory then it creates it
                if not os.path.isdir(os.path.join(dir, dir_name)):
                    os.mkdir(os.path.join(dir, dir_name))
                    
                source = dir + "/" + str(file)
                destination = dir + "/" + str(dir_name)

                shutil.move(source, destination)


                    
if __name__ == '__main__':
    # EX: /Users/your_name/Documents/folder
    path = input("Enter the full path to the folder you want to sort: ")
    sort_directory(path)
