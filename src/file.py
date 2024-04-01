class File:
    def __init__(self, file_path, size):
        self.file_path = file_path
        self.size = size

    def __repr__(self):
        return f"[path: {self.file_path}, size: {self.size}]"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.file_path == other.file_path and self.size == other.size
