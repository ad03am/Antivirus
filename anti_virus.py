class File:
    def __init__(self, name, path, status, hash):
        self._name = name
        self._path = path
        self._status = status
        self._hash = hash

    def name(self):
        return self._name

    def path(self):
        return self._path

    def status(self):
        return self._status

    def hash(self):
        return self._hash


class Directory:
    def __init__(self, name, path, files):
        self._name = name
        self._path = path
        self._files = files

    def name(self):
        return self._name

    def path(self):
        return self._path

    def files(self):
        return self._files
