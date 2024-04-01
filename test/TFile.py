from os import remove, makedirs, rmdir, symlink, unlink
from os.path import abspath, exists
import shutil

class TFile:
    file_folder = "test/.test_files"

    def __init__(self):
        self._files = []
        self._folders = []
        self._links = []
        if exists(TFile.file_folder):
            shutil.rmtree(TFile.file_folder)
        makedirs(TFile.file_folder)
    
    def create_folder(self, path):
        new_folder_path = TFile.file_folder + "/" + path
        self._folders.insert(0, new_folder_path)
        makedirs(new_folder_path)
        return path

    def create_file(self, path, content):
        new_file_path = TFile.file_folder + "/" + path
        self._files.append(new_file_path)
        f = open(new_file_path, "w")
        f.write(content)
        f.close()
        return abspath(new_file_path)
    
    def create_symlink(self, src, dst):
        new_symlink_path = abspath(TFile.file_folder + "/" + dst)
        self._links.append(new_symlink_path)
        symlink(abspath(TFile.file_folder + "/" + src), new_symlink_path)

    def __del__(self):
        pass
        for f in self._files:
            remove(f)
        for l in self._links:
            unlink(l)
        for d in self._folders:
            rmdir(d)
        rmdir(TFile.file_folder)
