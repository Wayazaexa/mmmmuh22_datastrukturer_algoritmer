import os

def searchFile(searchString, currentPath):
    try:
        with open(currentPath, 'r', encoding='utf-8') as file:
            if searchString in file.read():
                print(currentPath)
    except Exception as fileError:
        print(f"Error reading file: {currentPath}; {fileError}")

def filecrawler(searchString, searchPath):
    currentPath = None
    try:
        for filename in os.listdir(searchPath):
            currentPath = os.path.join(searchPath, filename)

            if os.path.isdir(currentPath):
                filecrawler(searchString, currentPath)
            elif os.path.isfile(currentPath):
                searchFile(searchString, currentPath)
    except Exception as folderError:
        print(f"Error reading folder: {searchPath}; {folderError}")

if __name__ == '__main__':

    # Set path
    path = os.path.join(os.getcwd(), '../TestData')
    # Normalize path (removes the unnecessary 'python/..' from the path)
    search_path = os.path.normpath(path)

    inputString = "y"
    while (inputString == "yes" or inputString == "y"):
        inputString = input("What do you want to search for? ")
        filecrawler(inputString, search_path)
        inputString = input("Do you want to search again (yes/y)? ")
