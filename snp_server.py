import tornado.ioloop
import tornado.web

import os


def remove_files() -> None:
    os.system('rm -rf uploads/*')
    os.system('rm -rf runs/*')


class MainHandler(tornado.web.RequestHandler):
    def get(self) -> None:
        self.render("main.html")


class UploadHandler(tornado.web.RequestHandler):
    def post(self) -> None:
        try:
            file = self.request.files['file'][0]
            output_file = open(f'{os.path.join(os.path.dirname(__file__))}'
                               f'/uploads/{file["filename"]}', 'wb')
            output_file.write(file['body'])

            # track.py
            os.system(f'python3 track.py --source uploads/{file["filename"]} '
                      f'--yolo_model weights.pt --save-vid')

            path_out = f'{os.path.join(os.path.dirname(__file__))}' \
                       f'/runs/track/weights_osnet_x0_25/'
            path_in = f'{os.path.join(os.path.dirname(__file__))}' \
                      f'/static/media/'
            print(f'cp {path_out}{file["filename"]} {path_in}')
            os.system(f'cp {path_out}{file["filename"]} {path_in}')
            os.system(f'rm -rf {path_out}{file["filename"]}')

            self.redirect("/")

        except Exception:
            print('Error: file have not been attached')


def make_app() -> tornado.web.Application:
    print('Server started')
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/upload', UploadHandler)],
        static_path=os.path.join(os.path.dirname(__file__), 'static'),
        template_path=os.path.join(os.path.dirname(__file__), 'templates')
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        remove_files()
        print('Server stopped')
