from flask import Flask, render_template
import os


class File:
    def __init__(self, filename, type):
        self.filename = filename
        self.link = None
        self.type = type

    def generate_link(self):
        filename = self.filename.replace(' ', '%20')
        self.link = f'/media/{self.type}s/{filename}'


app = Flask(
    __name__,
    static_folder='public',
    static_url_path='/'
)

@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/docs')
def get_docs():
    docs_names = os.listdir('public/media/docs')
    files = list()
    for name in docs_names:
        file = File(filename=name, type='doc')
        file.generate_link()
        files.append(file)
    return render_template('links.html', files=files)

@app.route('/imgs')
def get_imgs():
    imgs_names = os.listdir('public/media/imgs')
    files = list()
    for name in imgs_names:
        file = File(filename=name, type='img')
        file.generate_link()
        files.append(file)
    return render_template('links.html', files=files)

@app.route('/vids')
def get_vids():
    vids_names = os.listdir('public/media/vids')
    files = list()
    for name in vids_names:
        file = File(filename=name, type='vid')
        file.generate_link()
        files.append(file)
    return render_template('links.html', files=files)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2121)