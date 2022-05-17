import tornado.ioloop
import tornado.web
import os.path


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
        except Exception:
            print('Error: file have not been attached')

        self.redirect('http://localhost:8888/')


def make_app() -> tornado.web.Application:
    print('Server started')
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/upload', UploadHandler)],
        static_path=os.path.join(os.path.dirname(__file__),
                                 'static'),
        template_path=os.path.join(os.path.dirname(__file__),
                                   'templates'))


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print('Server stopped')
