import os
import shutil

path = os.getcwd()
files = os.listdir(path)

filesWithoutExt = [file.split('.')[0] for file in files]
probleme = list(set(filesWithoutExt))
probleme.remove('README')
probleme.remove(probleme[0])
probleme.remove('files_arrange')

print(probleme)
print(path)
for problema in probleme:
    try:
        os.mkdir(path + f'\\{problema}')
    except:
        continue

for file in files:
    if os.path.isfile(os.path.abspath(file)):
        if file.split('.')[0] in probleme:
            tmp = file.split('.')[0]
            newPath = os.path.join(path, f'{tmp}\\{file}')
            print(newPath)
            # print(f'old path: {os.path.abspath(file)}, new path: {newName}')
            # # file.close()
            shutil.move(os.path.abspath(file), newPath)