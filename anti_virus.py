import os
import argparse
import sys


class Directory:
    def __init__(self, path=None, files=None):
        self._path = path
        self._files = files

    def path(self):
        return self._path

    def files_in_dir(self):
        # funkcja dodająca nazwy plików do zmiennej
        self._files = os.listdir(f"{self._path}")
        self._files.sort()
        return self._files


class AntiVirus:
    def __init__(self, directory: Directory, index=None):
        self._directory = directory
        self._index = index

    def directory(self):
        return self._directory

    def index(self):
        return self._index

    def full_scan(self):
        # funkcja odpowiadająca za skanowanie wszystkich plików w folderze
        files = self._directory._files
        for i in files:
            self.remove(i, "tojestwirus")
        index = []
        for i in files:
            x = os.stat(f"{self._directory._path}/{i}").st_ctime
            index.append(f"{i} {self._directory._path}/{i} Checked {x}")
        with open(f"{self._index}", "w") as index_file:
            for ind in index:
                index_file.write(f"{ind}\n")

    def fast_scan(self):
        # funkcja odpowiadająca za skanowanie nowych i zmodyfikowanych plików w folderze
        index = []
        with open(f"{self._index}", "r") as index_file:
            line = index_file.readline().strip()
            split_line = line.split()
            while len(line) > 0:
                index.append(split_line[0])
                line = index_file.readline().strip()
                split_line = line.split()
            files = self._directory._files
            for i in range(len(files)):
                if index[i][-3:] == "MOD":
                    self.remove(files[i], "tojestwirus")
            index = []
            for i in files:
                x = os.stat(f"{self._directory._path}/{i}").st_ctime
                index.append(f"{i} {self._directory._path}/{i} Checked {x}")
            with open(f"{self._index}", "w") as index_file:
                for ind in index:
                    index_file.write(f"{ind}\n")

    def add_to_index(self):
        # funkcja odpowaidająca za dodanie do indeksu informacji o plikach
        files = self._directory._files
        index = []
        for i in files:
            x = os.stat(f"{self._directory._path}/{i}").st_ctime
            index.append(f"{i}MOD {self._directory._path}/{i} Modified/New {x}")
        with open(f"{self._index}", "w") as index_file:
            for ind in index:
                index_file.write(f"{ind}\n")

    def update_index(self):
        # funkcja odpowaidająca za aktualizacje indeksu
        with open(f"{self._index}", "r") as index_file:
            old_files = []
            old_time = []
            line = index_file.readline().strip()
            split_line = line.split()
            while len(line) > 0:
                old_files.append(split_line[0])
                old_time.append(split_line[3])
                line = index_file.readline().strip()
                split_line = line.split()
            new_files = self._directory._files
            new_index = []
            i = 0
            j = 0
            while j < len(new_files):
                x = float(os.stat(f"{self._directory._path}/{new_files[j]}").st_ctime)
                if i >= len(old_files):
                    # dodanie do indexu new_files[j]
                    #  jako nowy/zmodyfikowany
                    new_index.append(
                        f"{new_files[j]}MOD {self._directory._path}/{new_files[j]} Modified/New {x}"
                    )
                    j += 1
                elif old_files[i] == new_files[j]:
                    if float(old_time[i]) < x:
                        # dodanie do indexu new_files[j]
                        #  jako nowy/zmodyfikowany
                        new_index.append(
                            f"{new_files[j]}MOD {self._directory._path}/{new_files[j]} Modified/New {x}"
                        )
                    else:
                        # dodanie do indexu new_files[j]
                        #  jako niezmodyfikowany
                        new_index.append(
                            f"{new_files[j]} {self._directory._path}/{new_files[j]} Checked {x}"
                        )
                    i += 1
                    j += 1
                elif old_files[i] in new_files:
                    new_index.append(
                        f"{new_files[j]}MOD {self._directory._path}/{new_files[j]} Modified/New {x}"
                    )
                    # dodanie do indexu new_files[j]
                    #  jako nowy/zmodyfikowany
                    j += 1
                elif old_files[i][:-3] == new_files[j] and old_files[i][-3:] == "MOD":
                    # dodanie do indexu new_files[j]
                    #  jako nowy/zmodyfikowany
                    new_index.append(
                        f"{new_files[j]}MOD {self._directory._path}/{new_files[j]} Modified/New {x}"
                    )
                    i += 1
                    j += 1
                else:
                    i += 1
            with open(f"{self._index}", "w") as index_file:
                for ind in new_index:
                    index_file.write(f"{ind}\n")

    def remove(self, file, virus):
        # funkcja odpowaidająca za usuwanie wirusa z plików
        with open(f"{self._directory._path}/{file}", "r") as file_with_pot_vir:
            lines = file_with_pot_vir.readlines()
        with open(f"{self._directory._path}/{file}", "w") as file_without_vir:
            for line in lines:
                if line.strip() != virus:
                    file_without_vir.write(line)

    def file_lines(self, file):
        # funkcja zwracająca wszystkie linijki z pliku
        with open(f"{self._directory._path}/{file}", "r") as file_with_pot_vir:
            lines = file_with_pot_vir.readlines()
        new_lines = []
        for i in lines:
            new_lines.append(i.strip())
        return new_lines


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', default='test_folder')
    args = parser.parse_args()
    directory = Directory(args.directory)
    directory.files_in_dir()
    anti_virus = AntiVirus(directory, 'index.txt')
    anti_virus.add_to_index()
    end = 0
    while end != "end":
        end = input("Co chcesz zrobić?\n1. Zaktualizować pliki\n2. Pełny skan\n3. Szybki skan\n4. Zakończ\n")
        if end == "1":
            anti_virus.update_index()
        elif end == "2":
            anti_virus.update_index()
            anti_virus.full_scan()
        elif end == "3":
            anti_virus.update_index()
            anti_virus.fast_scan()
        elif end == "4":
            end = "end"
        else:
            print("Podaj prawidłowy numer!")


if __name__ == "__main__":
    main(sys.argv)
