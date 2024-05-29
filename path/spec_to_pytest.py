import os
from pathlib import Path

def spec_to_pytest(spec_file):
    print(f'=== spec_file: {spec_file} --- cwd: {os.getcwd()} ===')
    temp_tests_directory = 'temp_tests'
    
    spec_file_path = Path(spec_file)
    filename = spec_file_path.stem
    pytest_file = None
    rdir = ''
    if spec_file_path.is_relative_to(Path.cwd()):
        relative_path = os.path.relpath(spec_file, os.getcwd())
        print(f'path relative to cwd: {relative_path}')
    elif spec_file_path.is_relative_to(Path.home()):
        relative_path = os.path.relpath(spec_file, Path.home())
        rdir = 'home'
        print(f'path relative to home: {relative_path}')
    else:
        print(f'not relative path')
        parts = list(spec_file_path.parts)
        print(f'parts: {parts}')
        relative_path = os.path.sep.join(parts[1:])
        rdir = 'x'

    relative_path_directory = os.path.dirname(relative_path)
    print(f'directory: {relative_path_directory}')
    print(f'filename: {filename}')
    pytest_file = os.path.join(os.getcwd(), temp_tests_directory, rdir, relative_path_directory, f'test_{filename}.py')
    print(f'pytest_file: {pytest_file}')
    print('=============================================')
    return pytest_file

spec_to_pytest(os.path.join(os.getcwd(), 'specs/examples/demo_date_check.yml'))
spec_to_pytest(os.path.join(Path.home(), 'specs/examples/demo_date_check.yml'))
spec_to_pytest('/specs/examples/demo_date_check.yml')