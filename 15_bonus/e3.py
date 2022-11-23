from os import path
import shutil

files_dir = path.join(path.curdir, '15_bonus', 'files')

print(files_dir)

shutil.make_archive('output', 'zip', files_dir)
