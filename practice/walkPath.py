#! python3
import zipfile, os, shutil, sys, time

print('working:  ' + os.getcwd())

for folderName, subfolders, filenames in os.walk('C:\\Users\\brooney\\Documents\\RedWood\\Temp'):
    print('The current folder is: ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER: ' + subfolder)

        for filename in filenames:
            print('FILE: ' + filename)
            os.chdir('C:\\Users\\brooney\\Documents\\RedWood\\Temp')
            if os.path.getmtime(filename) > 172800:
                shutil.move(filename, 'C:\\Users\\brooney\\Downloads\\testMove')

for filename in filenames:
    print('FILE: ' + filename)
    

print(' ')
            


    
