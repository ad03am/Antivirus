import os
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


print(datetime.fromtimestamp(a))