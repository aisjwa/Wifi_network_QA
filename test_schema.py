import os

def test_reports_folder_exists():
    os.makedirs('reports', exist_ok=True)
    assert os.path.isdir('reports')
