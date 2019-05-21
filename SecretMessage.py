import os
def rename_files():
    fileList = os.listdir(r"/Users/Ryan/Downloads/prank")
    print(fileList)

    table = str.maketrans(dict.fromkeys('0123456789'))

    os.chdir(r"/Users/Ryan/Downloads/prank")
    for filename in fileList:
        os.rename(filename, filename.translate(table))

rename_files()