from __future__ import annotations
import os
from dataclasses import dataclass
from typing import List
from flask import Flask, render_template


MEDIA_DIR: str = 'public/media'
FILES_BLACKLIST: List[str] = ['.gitkeep', 'desktop.ini']


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
    def get_files(cls, dir_path: str, type: str) -> List[File]:
        filenames: List[str] = [filename for filename in os.listdir(dir_path) if filename not in FILES_BLACKLIST]
        return [File(filename, type).generate_link() for filename in filenames]


app = Flask(__name__, static_folder='public', static_url_path='/public')


@app.route('/')
def get_index():
    return render_template('index.html')


@app.route('/docs')
def get_docs():
    files: List[File] = File.get_files(f'{MEDIA_DIR}/docs', 'doc')
    return render_template('links.html', files=files)


@app.route('/imgs')
def get_imgs():
    files: List[File] = File.get_files(f'{MEDIA_DIR}/imgs', 'img')
    return render_template('links.html', files=files)


@app.route('/vids')
def get_vids():
    files: List[File] = File.get_files(f'{MEDIA_DIR}/vids', 'vid')
    return render_template('links.html', files=files)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2121, debug=True)
