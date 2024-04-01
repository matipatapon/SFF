import sys
from TFile import TFile
from os.path import dirname, realpath

sys.path.append(f"{dirname(realpath(__file__))}/../src")
from hasher import Hasher

def test_hash_file():
    t_file = TFile()
    file1_path = t_file.create_file("test1.txt", "abcd")
    file2_path = t_file.create_file("test2.txt", "abcd")
    file3_path = t_file.create_file("test3.txt", "abed")
    sut = Hasher()

    assert sut.hash(file1_path) == sut.hash(file2_path) != sut.hash(file3_path)
