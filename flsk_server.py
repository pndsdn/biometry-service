import os.path
from flask import Flask, \
    render_template, \
    redirect, \
    request, \
    send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = f'{os.path.join(os.path.dirname(__file__))}/uploads/'
MEDIA_FOLDER = f'{os.path.join(os.path.dirname(__file__))}' \
               f'/static/media/'
TRACK_FOLDER = f'{os.path.join(os.path.dirname(__file__))}' \
               f'/runs/track/weights_osnet_x0_25/'

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    if request.method == 'GET':
        return render_template('main.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))

        # track.py
        os.system(f'python3 track.py --source uploads/{filename} '
                  f'--yolo_model weights.pt --save-vid')
        os.system(f'rm -rf uploads/{filename}')

        track_file = f'{os.path.join(os.path.dirname(__file__))}' \
                     f'/runs/track/weights_osnet_x0_25/{filename}'

        os.system(f'cp {track_file} {MEDIA_FOLDER}')
        os.system('rm -rf runs/*')
        return send_from_directory(MEDIA_FOLDER, filename, as_attachment=True)

    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)

