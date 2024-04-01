from os.path import dirname, realpath
import sys
sys.path.append(f"{dirname(realpath(__file__))}/../src")
from same_file_seeker import SameFileSeeker
from file import File

def createFile(path, size):
    return File(path, size)

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

class FakeHasher:
    def __init__(self):
        self._calls = dict()
    
    def hash(self, path):
        return self._calls.pop(path)
    
    def expect_call(self, path, hash):
        self._calls[path] = hash

    def all_called(self):
        return len(self._calls) == 0
    

def test_same_file_seeker_should_return_nothing_when_no_files():
    sut = SameFileSeeker(FakeHasher())
    assert len(sut.seek([])) == 0

def test_same_file_seeker_should_return_same_files():
    fake_hasher = FakeHasher()
    sut = SameFileSeeker(fake_hasher)
    files = [File("file1.txt", 1), File("file2.txt", 1)]
    fake_hasher.expect_call("file1.txt", 5)
    fake_hasher.expect_call("file2.txt", 5)

    result = sut.seek(files)

    assert len(result) == 1
    assert file_lists_equal(result[0], files)
    assert fake_hasher.all_called()

def test_files_are_not_same_when_size_is_different():
    sut = SameFileSeeker(FakeHasher())
    files = [File("file1.txt", 1), File("file2.txt", 2)]

    result = sut.seek(files)

    assert len(result) == 0

def test_files_are_not_same_when_have_different_hash():
    fake_hasher = FakeHasher()
    sut = SameFileSeeker(fake_hasher)
    files = [File("file1.txt", 1), File("file2.txt", 1)]
    fake_hasher.expect_call("file1.txt", 6)
    fake_hasher.expect_call("file2.txt", 9)

    result = sut.seek(files)

    assert len(result) == 0
    assert fake_hasher.all_called()
