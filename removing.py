'''import os
from datetime import datetime


def remove(file, virus):
    with open(f'test_folder/{file}', 'r') as file_with_potential_virus:
        lines = file_with_potential_virus.readlines()
    with open(f'test_folder/{file}', 'w') as file_without_virus:
        for line in lines:
            if line.strip() != virus:
                file_without_virus.write(line)


def files_in_dir(directory):
    files = os.listdir(f'{directory}')
    files.sort()
    return files

def file_lines(file):
    with open(f'/home/ad03am/python/Anti-Virus/test_folder/{file}', 'r') as file_with_pot_virus:
        lines = file_with_pot_virus.readlines()
    new_lines = []
    for i in lines:
        new_lines.append(i.strip())
    return new_lines

print(files_in_dir('test_folder'))



class File:
    def __init__(self, name, path, status, hash):
        # status: new, modified, safe
        pass


def fileee(file):
    with open(f'test_folder/{file}', 'r') as file_with_potential_virus:
        lines = file_with_potential_virus.readlines()
        text = ''
        for line in lines:
            text += line
        return text


if fileee('test_file1.txt') == fileee('test_file2.txt'):
    print(True)


a = os.stat('test_folder/test_file1.txt').st_ctime
b = os.stat('test_folder/test_file2.txt').st_ctime
print(a, b)
print(datetime.fromtimestamp(a))
print(datetime.fromtimestamp(b))
if a > b:
    print(a-b)

files = ['test_file1.txt', 'test_file2.txt', 'test_file3.txt']
new_files = ['test_file1.txt', 'test_file2.txt', 'test_file3.txt', 'test_file4.txt', 'test_file5.txt']

# sort
i = 0
j = 0
# sprawdzenie która lista jest dłuższa -> ograniczenie pętli
while j < len(new_files):
    if i >= len(files):
        # dodanie do indexu new_files[j] jako nowy/zmodyfikowany
        j += 1
    elif files[i] == new_files[j]:
        # dodanie do indexu new_files[j] w zaleznosci od daty modyfikacji
        i += 1
        j += 1
    elif files[i] in new_files:
        # dodanie do indexu new_files[j] jako nowy/zmodyfikowany
        j += 1
    else:
        i += 1



with open(f'index.txt', 'r') as ind:
    old_index = []
    line = ind.readline().strip()
    while len(line) > 0:
        old_index.append(line)
        line = ind.readline().strip()
    print(old_index)
c = 'abcde'
print(c[-3:])'''