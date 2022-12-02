import zipfile
import os

def unpack_archive(arch_filepath, dest_dir):
    with zipfile.ZipFile(os.path.join(arch_filepath), 'r') as archive:
        archive.extractall(path=dest_dir)


if __name__ == '__main__':
    cur_dir = os.path.curdir
    files_dir = os.path.join(cur_dir, '18_bonus', 'files')
    for test_file in ['a.txt', 'b.txt']:
        filepath = os.path.join(files_dir, test_file)
        if os.path.isfile(filepath):
            os.remove(filepath)
    unpack_archive(arch_filepath=os.path.join(files_dir, 'compressed.zip'), dest_dir=files_dir)
