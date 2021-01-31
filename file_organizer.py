"""file_organizer.py
Author: Harman Suri
Jan 20, 2021

Description:    Organizes specific types of files, in the folder the program is
                currently in, into new folders labeled to correspond with the types
                of files it holds.
"""

import os


def move_file(file):
    """Given a list of files, those files are moved into new folders based
    on their file extension

    Args:
        file: a list of all files and folder in the current working directory

    """

    # creates paths for the current working directory
    # and the 3 new folders we want to move files into
    current_dir = os.getcwd()
    doc_dir = os.path.join(current_dir, 'Documents')
    img_dir = os.path.join(current_dir, 'Images')
    app_dir = os.path.join(current_dir, 'Applications')

    # lists of extensions for various types of files
    doc_file_exts = ['.txt', '.doc', '.docx', '.rtf', 'pdf']
    img_file_exts = ['.jpg', '.png', '.bpm', '.tiff']
    exe_file_exts = ['.exe']

    # if the extension of the current file is of a document
    # the file is moved into a Documents folder
    if os.path.splitext(file)[1] in doc_file_exts:
        # if a Documents folder doesn't exist, only then create a new one
        if not os.path.exists(doc_dir):
            os.makedirs(doc_dir)

        # rename current file name in order to move it to the Documents folder
        os.rename(os.path.join(current_dir, file), os.path.join(
            current_dir, os.path.join('Documents', file)))

    # the same is done for both image files and application files
    # by creating and moving those files into their respective folders
    elif os.path.splitext(file)[1] in img_file_exts:
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)

        os.rename(os.path.join(current_dir, file), os.path.join(
            current_dir, os.path.join('Images', file)))

    elif os.path.splitext(file)[1] in exe_file_exts:
        if not os.path.exists(app_dir):
            os.makedirs(app_dir)

        os.rename(os.path.join(current_dir, file), os.path.join(
            current_dir, os.path.join('Applications', file)))


# gets a list of all files and folders in the current working directory
files = os.listdir()

# for every file in the current directory
# move the file, as long as it is not this program
for file in files:
    if file != 'file_organizer.py':
        move_file(file)
