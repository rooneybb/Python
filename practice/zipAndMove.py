#! python3
import zipfile, os, shutil, sys, time

print('working:  ' + os.getcwd())

for folderName, subfolders, filenames in os.walk('C:\\Users\\brooney\\Documents\\RedWood\\Test'):
    print('The current folder is: ' + folderName)

    for subfolder in subfolders:
        #print('SUBFOLDER: ' + subfolder)
        continue

        for filename in filenames:
            print('FILE: ' + filename + os.path.getmtime(filename))
            #os.chdir('C:\\Users\\brooney\\Documents\\RedWood\\Test')
            #if os.path.getmtime(filename) > 172800:
                #shutil.move(filename, 'C:\\Users\\brooney\\Downloads\\testMove')

timestr = time.strftime('%Y%m%d')
zipFileName = 'archive_' + timestr + '.zip'

for filename in filenames:    
    os.chdir('C:\\Users\\brooney\\Documents\\RedWood\\Test')
    #os.walk('C:\\Users\\brooney\\Documents\\RedWood\\Test')
    #print('FILE: ' + filename + os.path.getmtime(filename)) 
    if os.path.getmtime(filename) > 172800.00: 
        backupZip = zipfile.ZipFile(zipFileName, mode = 'a') 
        backupZip.write(filename)
        #shutil.move(filename, 'C:\\Users\\brooney\\Downloads\\testMove')
    backupZip.close()


