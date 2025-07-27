from flask import Flask, request, send_from_directory, render_template, jsonify
from werkzeug.utils import secure_filename
from datetime import datetime
from pathlib import Path
import mimetypes

app = Flask(__name__)
UPLOAD_FOLDER = Path("uploads")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

UPLOAD_FOLDER.mkdir(exist_ok=True)


### Template Filters ###
@app.template_filter('file_size')
def file_size_filter(path):
    return Path(path).stat().st_size if Path(path).exists() else 0

@app.template_filter('file_mtime')
def file_mtime_filter(path):
    return Path(path).stat().st_mtime if Path(path).exists() else 0

@app.template_filter('datetimeformat')
def datetimeformat(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%b %d, %Y %I:%M %p')

@app.template_filter('truncate_filename')
def truncate_filename(filename, max_length=25):
    if len(filename) <= max_length:
        return filename
    name, ext = Path(filename).stem, Path(filename).suffix
    return f"{name[:12]}...{name[-5:]}{ext}"

@app.template_filter('filesizeformat')
def filesizeformat(size):
    for unit in ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if size < 1024.0:
            return f"{int(size)} {unit}" if unit == 'bytes' else f"{size:.1f} {unit}"
        size /= 1024.0


### Utility ###
def is_previewable(filename):
    mime_type, _ = mimetypes.guess_type(filename)
    return mime_type and mime_type.split('/')[0] in ['text', 'image', 'video', 'audio']


### Routes ###
@app.route('/')
def index():
    files = []
    for file in UPLOAD_FOLDER.iterdir():
        if file.is_file():
            files.append({
                'name': file.name,
                'size': file.stat().st_size,
                'mtime': file.stat().st_mtime,
                'preview': is_previewable(file.name)
            })
    files.sort(key=lambda x: x['mtime'], reverse=True)
    return render_template('index.html', files=files, upload_folder=str(UPLOAD_FOLDER))


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if not file or file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    filename = secure_filename(file.filename)
    file.save(UPLOAD_FOLDER / filename)
    return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200


@app.route('/preview/<filename>')
def preview_file(filename):
    if not filename.lower().endswith('.pdf'):
        return "Preview not supported for this file type.", 400
    return render_template('preview.html', filename=filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(str(UPLOAD_FOLDER), filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
