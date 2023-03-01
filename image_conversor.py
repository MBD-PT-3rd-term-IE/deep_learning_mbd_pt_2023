import os
import glob
from PIL import Image
import PIL

#Please select the path of the folder where the images are located via input user
path = input('Please select the path of the folder where the images are located: ')

#list all the files in the directory
files = os.listdir(path)

#print all these files will be converted, make sure jpg is used
print('These files will be converted, make sure only jpg format is used: ', files)

#Please select the path of the folder where the images will be saved
path2 = input('Please select the path of the folder where the images are located: ')


#loop through the files and change the resolution saving the new file in the same directory with a new name
for file in files:
    img = Image.open(path + '\\' + file)
    img = img.resize((416,416), Image.ANTIALIAS)
    img.save(path2 + '\\' + file + '_416x416.jpg')

#check the new resolution
print('Cheking the new resolution...')
img = Image.open(path2 + '\\' + file + '_416x416.jpg')
img.size

