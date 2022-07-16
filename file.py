from __future__ import annotations
import os
from dataclasses import dataclass
from typing import List
from config import MEDIA_DIR, FILES_BLACKLIST


@dataclass
class File:
    filename: str
    type: str
    link: str = None

    def generate_link(self) -> File:
        filename: str = self.filename.replace(' ', '%20')
        self.link = f'{MEDIA_DIR}/{self.type}s/{filename}'
        return self

    @classmethod
    def get_files(cls, type: str) -> List[File]:
        filenames: List[str] = [filename for filename in os.listdir(f'{MEDIA_DIR}/{type}s')
                                if filename not in FILES_BLACKLIST]
        return [File(filename, type).generate_link() for filename in filenames]
