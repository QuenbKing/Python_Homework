import os
from typing import TextIO


class File:

    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self) -> TextIO:
        if os.path.exists(self.filename):
            self.file = open(self.filename, self.mode, encoding='UTF-8')
        else:
            print('Данного файла не существует. Был создан файл в режиме записи (write)')
            self.file = open(self.filename, 'w', encoding='UTF-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True
