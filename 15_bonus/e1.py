from os import path
import glob

myfiles = glob.glob(path.join(path.curdir, '15_bonus', 'files', '*.txt'))

print(myfiles)

for filepath in myfiles:
    with open(filepath, 'r') as f:
        print(f.read().upper())