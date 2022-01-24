from anti_virus import AntiVirus, Directory


def test_removing():
    # test sprawdzający usunięcie wirusa z jednego pliku
    directory = Directory('test_folder_2')
    anti_virus = AntiVirus(directory, 'index2.txt')
    anti_virus.remove('test_file2.txt', 'wirus')
    assert 'wirus' not in anti_virus.file_lines('test_file2.txt')


def test_full_scan():
    # test sprawdzający usunięcie wirusa ze wszystkich plików w folderze
    directory = Directory('test_folder_2')
    directory.files_in_dir()
    anti_virus = AntiVirus(directory, 'index2.txt')
    anti_virus.full_scan()
    assert 'wirus' not in anti_virus.file_lines('test_file4.txt')


def test_fast_scan():
    # test sprawdzający usunięcie wirusa ze wszystkich plików w folderze
    directory = Directory('test_folder_2')
    directory.files_in_dir()
    anti_virus = AntiVirus(directory, 'index2.txt')
    anti_virus.fast_scan()
    assert 'wirus' not in anti_virus.file_lines('test_file4.txt')


def test_files_in_dir():
    # test sprawdzający dodawanie nazw plików do zmiennej
    directory = Directory('test_folder_2')
    files = directory.files_in_dir()
    assert files == ['test_file1.txt', 'test_file2.txt',
                     'test_file3.txt', 'test_file4.txt', 'test_file5.txt']


def test_index():
    # test sprawdzający tworzenie indeksu
    directory = Directory('test_folder_2')
    directory.files_in_dir()
    anti_virus = AntiVirus(directory, 'index2.txt')
    anti_virus.add_to_index()
    with open('index2.txt', 'r') as file:
        line = file.readline().strip()
        parts = line.split()
        assert parts[0] == 'test_file1.txtMOD'
        assert parts[1] == 'test_folder_2/test_file1.txt'
        assert parts[2] == 'Modified/New'


def test_update_index():
    # test sprawdzający aktualizacje indeksu
    directory = Directory('test_folder_2')
    directory.files_in_dir()
    anti_virus = AntiVirus(directory, 'index2.txt')
    anti_virus.add_to_index()
    anti_virus.full_scan()
    anti_virus.update_index()
    with open('index2.txt', 'r') as file:
        line = file.readline().strip()
        parts = line.split()
        assert parts[0] == 'test_file1.txt'
        assert parts[1] == 'test_folder_2/test_file1.txt'
        assert parts[2] == 'Checked'


