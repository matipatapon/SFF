import hashlib

class Hasher:
    def hash(self, file_path):
        file_hash = hashlib.md5()
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                file_hash.update(chunk)
        return file_hash.hexdigest()
