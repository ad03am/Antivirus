from anti_virus import AntiVirus


def test_removing():
    anti_virus = AntiVirus('test_folder')
    anti_virus.remove('test_file2.txt', 'wirus')
    assert 'wirus' not in anti_virus.file_lines('test_file2.txt')


def test_virus():
    anti_virus = AntiVirus('test_folder')
    assert 'wirus' in anti_virus.file_lines('test_file3.txt')


def test_full_scan():
    anti_virus = AntiVirus('test_folder')
    anti_virus.full_scan()
    assert 'wirus' not in anti_virus.file_lines('test_file3.txt')
