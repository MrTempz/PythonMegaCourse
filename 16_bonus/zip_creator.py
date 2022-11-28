import zipfile
import os

def make_archive(filepaths, dest_dir):
    with zipfile.ZipFile(os.path.join(dest_dir, 'compressed.zip'), 'w') as archive:
        for filepath in filepaths:
            archive.write(filepath, arcname=os.path.basename(filepath))


if __name__ == '__main__':
    cur_dir = os.path.curdir
    files_dir = os.path.join(cur_dir, '16_bonus', 'files')
    if os.path.isfile(os.path.join(files_dir, 'compressed.zip')):
        os.remove(os.path.join(files_dir, 'compressed.zip'))
    make_archive(filepaths=[os.path.join(files_dir, 'a.txt'), os.path.join(files_dir, 'b.txt')], dest_dir=files_dir)
