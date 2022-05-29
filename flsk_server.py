import os.path
from flask import Flask, \
    render_template, \
    redirect, \
    request, \
    send_from_directory, \
    flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = f'{os.path.join(os.path.dirname(__file__))}/uploads/'
MEDIA_FOLDER = f'{os.path.join(os.path.dirname(__file__))}' \
               f'/static/media/'
TRACK_FOLDER = f'{os.path.join(os.path.dirname(__file__))}' \
               f'/runs/track/weights_osnet_x0_25/'
VIDEO_FORMATS = ['asf', 'avi', 'gif', 'm4v', 'mkv', 'mov',
                 'mp4', 'mpeg', 'mpg', 'ts', 'wmv']

app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/', methods=['GET'])
def root():
    if request.method == 'GET':
        return render_template('main.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))

        if filename.split('.')[1] not in VIDEO_FORMATS:
            os.system(f'rm -rf uploads/{filename}')
            return redirect('/')

        # track.py
        os.system(f'python3 track.py --source uploads/{filename} '
                  f'--yolo_model weights.pt --save-vid')
        os.system(f'rm -rf uploads/{filename}')

        os.system(f'cp {TRACK_FOLDER}{filename} {MEDIA_FOLDER}')
        os.system('rm -rf runs/*')
        return send_from_directory(MEDIA_FOLDER, filename, as_attachment=True)

    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
