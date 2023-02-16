import os

# Current working directory
cwd = os.getcwd()

# Relative directory
# Ni kan behöva ändra denna. Beror på var ni kör python ifrån.
search_path = os.path.join(cwd,'..','TestData')

if __name__ == '__main__':
    if os.path.isdir(search_path):
        print("./TestData is a directory")
    
    if not os.path.isfile(search_path):
        print("Hence it is not a regular file")
    
    current_path = None
    for filename in os.listdir(search_path):
        current_path = os.path.join(search_path, filename)
        print(current_path)

    with open(current_path, 'r', encoding='utf-8') as f:
        print(f.read())