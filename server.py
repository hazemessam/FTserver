from typing import List
from flask import Flask, render_template, send_from_directory
from file import File
from config import MEDIA_DIR


app = Flask(__name__, static_url_path='/')


@app.route('/')
def get_index():
    return render_template('index.html')


@app.route('/docs')
def get_docs():
    files: List[File] = File.get_files('doc')
    return render_template('links.html', files=files)


@app.route('/imgs')
def get_imgs():
    files: List[File] = File.get_files('img')
    return render_template('links.html', files=files)


@app.route('/vids')
def get_vids():
    files: List[File] = File.get_files('vid')
    return render_template('links.html', files=files)


@app.route('/media/<path:file_path>')
def downloads(file_path):
    return send_from_directory(MEDIA_DIR, file_path, as_attachment=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2121, debug=True)
