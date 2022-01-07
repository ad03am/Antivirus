from anti_virus import AntiVirus


def test_removing():
    # test sprawdzający usunięcie wirusa z jednego pliku
    anti_virus = AntiVirus('test_folder')
    anti_virus.remove('test_file2.txt', 'wirus')
    assert 'wirus' not in anti_virus.file_lines('test_file2.txt')


def test_virus():
    # test sprawdzający czy antywirus widzi wirusa w pliku
    anti_virus = AntiVirus('test_folder_2')
    assert 'wirus' in anti_virus.file_lines('test_file3.txt')


def test_full_scan():
    # test sprawdzający usunięcie wirusa ze wszystkich plików w folderze
    anti_virus = AntiVirus('test_folder')
    anti_virus.full_scan()
    assert 'wirus' not in anti_virus.file_lines('test_file4.txt')
