from os.path import dirname, realpath, abspath
from TFile import TFile
import sys

sys.path.append(f"{dirname(realpath(__file__))}/../src")
from file_collector import FileCollector
from file import File

def file_lists_equal(list1, list2):
    if len(list1) != len(list2):
        return False

    for f1 in list1:
        f1_in_l2 = False
        for f2 in list2:
            if f1 == f2:
                f1_in_l2 = True
                break
        if not f1_in_l2:
            return False
    return True

def createFile(path, size):
    return File(abspath(TFile.file_folder + "/" + path), size)

def test_file_collector_should_collect_file():
    t_file = TFile()
    t_file.create_file("test.txt", "abcdefg")
    sut = FileCollector()

    files = sut.collect(TFile.file_folder)

    assert len(files) == 1
    assert files[0] == createFile("test.txt", 7)

def test_file_collector_should_collect_files():
    t_file = TFile()
    t_file.create_file("test1.txt", "abc")
    t_file.create_file("test2.txt", "abcd")
    t_file.create_folder("testfolder")
    t_file.create_file("testfolder/test3.txt", "abcde")
    sut = FileCollector()

    files = sut.collect(TFile.file_folder)
    assert file_lists_equal(files, [createFile("/test1.txt", 3), 
                                    createFile("/test2.txt", 4),
                                    createFile("/testfolder/test3.txt", 5)])

def test_file_collector_should_ignore_symlink():
    t_file = TFile()
    t_file.create_file("test1.txt", "abc")
    t_file.create_symlink("test1.txt", "symlink.txt")
    sut = FileCollector()

    files = sut.collect(TFile.file_folder)

    assert file_lists_equal(files, [createFile("/test1.txt", 3)])
