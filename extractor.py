from openpyxl import load_workbook
from openpyxl.cell import Cell
from openpyxl.worksheet.worksheet import Worksheet
from typing import Tuple
from os.path import join
from os import makedirs

wb = load_workbook(filename='python spreadsheet.xlsx')
sheet_ranges: Worksheet = wb['Result 1']
column_names = []
album = {}

row: Tuple[Cell, ...]
for row in sheet_ranges.rows:
    if row[0].row == 1:
        for cell in row:
            column_names.append(cell.value)
        continue

    cell_dict = {}

    album_id = row[4].value
    if album_id not in album:
        album[album_id] = []

    for index, cell in enumerate(row):
        column_name = column_names[index]
        cell_dict[column_name] = cell.value

    album[album_id].append(cell_dict)

for album_id, files in album.items():
    for file in files:
        album_id = str(album_id)
        makedirs(join('albums', album_id, file['display_name']), exist_ok=True)
        open(join('albums', album_id, file['display_name'], 'code.py'), 'w').write(file['code'])
        if file['result']:
            open(join('albums', album_id, file['display_name'], 'result.txt'), 'w').write(file['result'])
        open(join('albums', album_id, file['display_name'], 'created.txt'), 'w').write(file['created'])
