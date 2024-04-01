class SameFileSeeker:
    def __init__(self, file_hasher):
        self._file_hasher = file_hasher

    def seek(self, files):
        files_to_size = dict()
        for f in files:
            if f.size in files_to_size:
                files_to_size[f.size].append(f)
            else:
                files_to_size[f.size] = [f]

        result = []
        files_to_hash = dict()
        for files in files_to_size.values():
            if len(files) < 2:
                    continue
            for f in files:
                hash = self._file_hasher.hash(f.file_path)
                if hash in files_to_hash:
                    files_to_hash[hash].append(f)
                else:
                    files_to_hash[hash] = [f]
            
        for files in files_to_hash.values():
            if len(files) > 1:
                result.append(files)
        return result
