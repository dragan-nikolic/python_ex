"""
2024-05-27 by Dragan

Reference: https://www.freecodecamp.org/news/how-to-use-pathlib-module-in-python/
"""

import pathlib

p1 = pathlib.Path(__file__)
print(f'===== pathlib.Path(__file__): {p1} =====')
print(f'type: {type(p1)}')
print(f"str: {str(p1)}")
print(f'name: {p1.name}')
print(f'parts: {p1.parts}')
print(f'anchor: {p1.anchor}')
print(f'drive: {p1.drive}')
print(f'parent: {p1.parent}')
print('---------------------------')
print(f'cwd(): {p1.cwd()}')
print(f'exists(): {p1.exists()}')
print(f'home(): {p1.home()}')
print(f'is_absolute(): {p1.is_absolute()}')
print(f'is_relative_to(): {p1.is_relative_to(p1.cwd())}')
print(f'parents[0]: {p1.parents[0]}')
print(f'parents.count[0]: {p1.parents.count(0)}')
print(f'name: {p1.name}')

p2str = 'path/pathlib_ex.py'
p2 = pathlib.Path(f'{p2str}')
print(f"===== pathlib.Path('{p2str}'): {p2} =====")
print(f"str: {str(p2)}")
print(f'name: {p2.name}')
print(f'parts: {p2.parts}')
print(f'anchor: {p2.anchor}')
print('---------------------------')
print(f'is_absolute(): {p2.is_absolute()}')
print(f'absolute(): {p2.absolute()}')

p3str = 'path/unknown_file.py'
p3 = pathlib.Path(f'{p3str}')
print(f"===== pathlib.Path('{p3str}'): {p3} =====")
print(f'name: {p3.name}')
print(f'parts: {p3.parts}')
print('---------------------------')
print(f'exists(): {p3.exists()}')
