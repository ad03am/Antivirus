import os

from removing import remove


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
    def __init__(self, path=None, files=None):
        self._path = path
        self._files = files

    def path(self):
        return self._path

    def files_in_dir(self):
        self._files = os.listdir(f'{self._path}')
        self._files.sort()
        return self._files


class AntiVirus:
    def __init__(self, directory: Directory):
        self._directory = directory

    def directory(self):
        return self._directory

    def full_scan(self):
        # files = os.listdir(f'{self._directory}')
        files = self._directory._files
        for i in files:
            remove(i, 'wirus')

    def fast_scan(self):
        # files = os.listdir(f'{self._directory}')
        files = self._directory._files
        for i in files:
            remove(i, 'wirus')

    def index(self):
        # dodać scieżki, stan pliku i hash
        files = self._directory._files
        self._index = []
        for i in range(len(files)):
            self._index.append(f'{i}{files[i][(len(files[i])//2):]}')
        return self._index

    def remove(self, file, virus):
        with open(f'{self._directory._path}/{file}', 'r') as file_with_pot_virus:
            lines = file_with_pot_virus.readlines()
        with open(f'{self._directory._path}/{file}', 'w') as file_without_virus:
            for line in lines:
                if line.strip() != virus:
                    file_without_virus.write(line)

    def file_lines(self, file):
        with open(f'{self._directory._path}/{file}', 'r') as file_with_pot_virus:
            lines = file_with_pot_virus.readlines()
        new_lines = []
        for i in lines:
            new_lines.append(i.strip())
        return new_lines


if __name__ == "__main__":
    pass
