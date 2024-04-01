from file_collector import FileCollector
from same_file_seeker import SameFileSeeker
from hasher import Hasher
from os.path import exists
from sys import argv

file_collector = FileCollector()
same_file_seeker = SameFileSeeker(Hasher())

assert len(argv) == 2
assert exists(argv[1])
directory = argv[1]
identical_files = same_file_seeker.seek(file_collector.collect(directory))

identical_files.sort(key=lambda files : files[0].size, reverse=True)

for files in identical_files:
    print(f"GROUP, ONE FILE SIZE {round(files[0].size / (1024 * 1024 * 8), 2)}MB")
    for f in files:
        print(f"{f.file_path}")
    print("\n")
