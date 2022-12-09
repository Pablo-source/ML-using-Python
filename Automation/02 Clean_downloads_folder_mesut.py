import os
import shutil

if __name__ == '__main__': ##i don't undestand https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    _dir = r'C:\Users\mesut.uzunov\OneDrive - NHS England\Training\Test Python 3 folder'
    os.chdir(_dir) # changes current working directory to the downloads folder
    split_types = ['pdf', 'csv', 'pptx']
    files_to_move = []
    print(f'File in directory={_dir}  , files=\n{os.listdir(os.curdir)}')
    # List items in the selected path (current directory, which was defined above)
    # Add all files in the current working directory into a list
    for file in os.listdir(os.curdir):
        if os.path.isdir(file): #here so script doesn't stop after coming to a file
            continue
        files_to_move.append(file)
        #split_types.append(file.split('.')[-1])
    print(f'Files to move={files_to_move}')
    print(f'Split types={split_types}')

# A loop to go through the file types in split_types and create a folder if the folder doesn't exist
    for type in split_types:
        if not os.path.isdir(type):  # Returns True or False. If false then go to next line
            print(f'Dir I will create={os.path.join(os.curdir, type)}')
            os.makedirs(os.path.join(os.curdir, type))

 # Move in the created directories
    for file in files_to_move:
        if os.path.isdir(file): # Here so script doesn't stop after coming to a file
            continue
        _from = os.path.join(os.curdir, file)
        _to = os.path.join(os.curdir, file.split('.')[-1], file)
        print(f'Moving file={_from} to {_to}')
        os.rename(_from, _to)