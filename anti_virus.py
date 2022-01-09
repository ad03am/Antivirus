import os


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
    def __init__(self, directory: Directory, index=None, time=None):
        self._directory = directory
        self._index = index
        self._time = time

    def directory(self):
        return self._directory

    def index(self):
        return self._index

    def time(self):
        return self._time

    def full_scan(self):
        # files = os.listdir(f'{self._directory}')
        files = self._directory._files
        for i in files:
            self.remove(i, 'wirus')

    def fast_scan(self):
        # files = os.listdir(f'{self._directory}')
        files = self._directory._files
        for i in files:
            self.remove(i, 'wirus')

    def add_to_index(self):
        # dodać scieżki, stan pliku i hash
        files = self._directory._files
        index = []
        time = []
        for i in files:
            index.append(f'{i}MOD')
            x = os.stat(f'{self._directory._path}/{i}').st_ctime
            time.append(x)
        with open(f'{self._index}', 'w') as index_file:
            for ind in index:
                index_file.write(f'{ind}\n')
        with open(f'{self._time}', 'w') as time_file:
            for t in time:
                time_file.write(f'{t}\n')

    def update_index(self):
        with open(f'{self._index}', 'r') as index_file:
            with open(f'{self._time}', 'r') as time_file:
                old_files = []
                old_time = []
                line = index_file.readline().strip()
                while len(line) > 0:
                    old_files.append(line)
                    line = index_file.readline().strip()
                new_line = time_file.readline().strip()
                while len(new_line) > 0:
                    old_time.append(new_line)
                    new_line = time_file.readline().strip()
                new_files = self._directory._files
                new_index = []
                i = 0
                j = 0
                while j < len(new_files):
                    if i >= len(old_files):
                        # dodanie do indexu new_files[j] jako nowy/zmodyfikowany
                        new_index.append(f'{new_files[j]}MOD')
                        j += 1
                    elif old_files[i] == new_files[j]:
                        x = str(os.stat(f'{self._directory._path}/{new_files[j]}').st_ctime)
                        if float(old_time[i]) < float(os.stat(f'{self._directory._path}/{new_files[j]}').st_ctime):
                            # dodanie do indexu new_files[j] jako nowy/zmodyfikowany
                            new_index.append(f'{new_files[j]}MOD')
                        else:
                            # dodanie do indexu new_files[j] jako niezmodyfikowany
                            new_index.append(f'{new_files[j]}')
                        i += 1
                        j += 1
                    elif old_files[i] in new_files:
                        new_index.append(f'{new_files[j]}MOD')
                        # dodanie do indexu new_files[j] jako nowy/zmodyfikowany
                        j += 1
                    elif old_files[i][:-3] == new_files[j] and old_files[i][-3:] == 'MOD':
                        # dodanie do indexu new_files[j] jako nowy/zmodyfikowany
                        new_index.append(f'{new_files[j]}MOD')
                        i += 1
                        j += 1
                    else:
                        i += 1
                with open(f'{self._index}', 'w') as index_file:
                    for ind in new_index:
                        index_file.write(f'{ind}\n')
                time = []
                for i in new_files:
                    x = os.stat(f'{self._directory._path}/{i}').st_ctime
                    time.append(x)
                with open(f'{self._time}', 'w') as time_file:
                    for t in time:
                        time_file.write(f'{t}\n')

    def remove(self, file, virus):
        with open(f'{self._directory._path}/{file}', 'r') as file_with_pot_vir:
            lines = file_with_pot_vir.readlines()
        with open(f'{self._directory._path}/{file}', 'w') as file_without_vir:
            for line in lines:
                if line.strip() != virus:
                    file_without_vir.write(line)

    def file_lines(self, file):
        with open(f'{self._directory._path}/{file}', 'r') as file_with_pot_vir:
            lines = file_with_pot_vir.readlines()
        new_lines = []
        for i in lines:
            new_lines.append(i.strip())
        return new_lines


if __name__ == "__main__":
    directory = Directory('test_folder')
    directory.files_in_dir()
    anti_virus = AntiVirus(directory, 'index.txt', 'time.txt')
    anti_virus.add_to_index()
    a = input('czy?')
    if a == 'a':
        anti_virus.update_index()
    print('Done')