import sys
import os
from PIL import Image

# grab first and second arguments
main_folder, new_copy = sys.argv[1], sys.argv[2]
# main_folder = input()
# new = input()
# new_copy = new


# os.chdir(main_folder)
# print(os.getcwd())
# os.chdir("..") # 
# print(os.getcwd())
# os.chdir(new)
# print(os.getcwd())
# #print(os.listdir())
# os.chdir("..")
# print(os.getcwd())
# os.chdir(new)
# print(os.getcwd())
# exit()
# check if new exsists if no create one
if not os.path.exists(new_copy):
    os.mkdir(new_copy)

# loop through pokedex and convert to png
for filename in os.listdir(main_folder):
    f = os.path.join(main_folder,filename)
    if os.path.isfile(f):
        img = Image.open(f)
        # that one!
        os.chdir(new_copy)
        clean_name = os.path.splitext(filename)[0]
        clean_name = os.path.splitext(clean_name)[0]
        img.save(f'{clean_name}.png', 'png')
        os.chdir("..")


