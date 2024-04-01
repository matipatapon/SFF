from os import walk, stat
from os.path import isfile, abspath, islink
from file import File

class FileCollector:
    def collect(self, path):
        files = []
        for (dirpath, dirnames, filenames) in walk(path):
            for file_name in filenames:
                file_path = abspath(dirpath + "/" + file_name)
                if isfile(file_path) and not islink(file_path):
                    stats = stat(file_path)
                    file = File(file_path, stats.st_size)
                    files.append(file)
        return files
