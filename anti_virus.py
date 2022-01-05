import os

from removing import remove

# tekst


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

    def files(self):
        return self._files

    def files_in_dir(self):
        self._files = os.listdir(f'{self._path}')
        return self._files


class AntiVirus:
    def __init__(self, directory):
        self._directory = directory

    def directory(self):
        return self._directory

    def full_scan(self):
        # files = os.listdir(f'{self._directory}')
        files = Directory.files_in_dir()
        for i in files:
            remove(i, 'wirus')

    def index(self):
        # dodać scieżki, stan pliku i hash
        files = Directory.files_in_dir()
        self._index = []
        for i in files:
            self._index.append([i])
        return self._index

    def remove(self, file, virus):
        with open(f'{self._directory}/{file}', 'r') as file_with_pot_virus:
            lines = file_with_pot_virus.readlines()
        with open(f'{self._directory}/{file}', 'w') as file_without_virus:
            for line in lines:
                if line.strip() != virus:
                    file_without_virus.write(line)

    def file_lines(self, file):
        with open(f'{self._directory}/{file}', 'r') as file_with_pot_virus:
            lines = file_with_pot_virus.readlines()
        new_lines = []
        for i in lines:
            new_lines.append(i.strip())
        return new_lines
