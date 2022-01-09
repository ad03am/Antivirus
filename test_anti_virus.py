from anti_virus import AntiVirus, Directory


def test_removing():
    # test sprawdzający usunięcie wirusa z jednego pliku
    directory = Directory('test_folder')
    anti_virus = AntiVirus(directory)
    anti_virus.remove('test_file2.txt', 'wirus')
    assert 'wirus' not in anti_virus.file_lines('test_file2.txt')


def test_full_scan():
    # test sprawdzający usunięcie wirusa ze wszystkich plików w folderze
    directory = Directory('test_folder_2')
    directory.files_in_dir()
    anti_virus = AntiVirus(directory)
    anti_virus.full_scan()
    assert 'wirus' not in anti_virus.file_lines('test_file4.txt')


def test_files_in_dir():
    directory = Directory('test_folder')
    files = directory.files_in_dir()
    assert files == ['test_file1.txt', 'test_file2.txt', 'test_file3.txt', 'test_file4.txt', 'test_file5.txt']


def test_index():
    directory = Directory('test_folder_2')
    directory.files_in_dir()
    anti_virus = AntiVirus(directory, 'index.txt', 'time.txt')
    anti_virus.add_to_index()


def test_update_index():
    directory = Directory('test_folder_2')
    directory.files_in_dir()
    anti_virus = AntiVirus(directory, 'index.txt')
    anti_virus.add_to_index()
