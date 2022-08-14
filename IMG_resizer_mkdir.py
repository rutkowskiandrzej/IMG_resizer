#! /usr/bin/env python3

import glob
import os
from PIL import Image

# making directory for resized photos
main_path = os.getcwd()
new_dir_path = os.getcwd() + r"\python_resized"
save_path = main_path + r"\python_resized"

# set terminal size
terminal_width = [len(link) for link in glob.glob(main_path + r"\*")]
cmd = f'mode {max(terminal_width)+70},20'
os.system(cmd)

try:
    os.mkdir(new_dir_path)
except OSError:
    print("Nieudane utworzenie folderu: %s " % new_dir_path)
else:
    print("Pomyślnie utworzono folder: %s " % new_dir_path)

# Image resize
answer = input("Podaj ilość pikseli dłuższego boku zdjęcia po zmianie (domyślnie jest 1600): ")

print('\n')

if answer.isnumeric() and int(answer):
    LARGER_DIM = int(answer)
else:
    LARGER_DIM = 1600

# resize part
increment = 0
for link in glob.glob(main_path + r"\*"):
    if link.lower().endswith('.png') or link.lower().endswith('.jpg') or link.lower().endswith('.jpeg'):

        with Image.open(link) as im:
            ratio = float(im.size[0]) / float(im.size[1])
            if ratio > 1:
                target_size = (LARGER_DIM, int(LARGER_DIM/ratio))
            else:
                target_size = (int(LARGER_DIM*ratio), LARGER_DIM)

            im2 = im.resize(target_size)
            im2_path = f'{save_path}' + '\\' + link.split('\\')[-1][:-4] + '_resized_' + f'{increment}' + link[-4:]
            im2.save(im2_path)
            mbytesize = os.path.getsize(im2_path) / 10 ** 6

        increment += 1

        print(f'- {mbytesize:.2f} MB -- {im2.size[0]}x{im2.size[1]} -' + 3*' ' + im2_path)
    else:
        pass

if increment == 0:
    print('Brak zdjęć do zmniejszenia w folderze! Usuwam wcześniej utworzony folder pomocniczy.')
    os.rmdir(new_dir_path)
    
input("\n\nAby zakończyć, naciśnij klawisz Enter.")
