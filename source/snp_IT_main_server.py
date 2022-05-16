import tornado.ioloop
import tornado.web
import os.path
import cv2


class MainHandler(tornado.web.RequestHandler):
    def get(self) -> None:
        self.render("main.html")


class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        file = self.request.files['file']
        print(file[0]['filename'])
        self.redirect('http://localhost:8888/')



def make_app() -> tornado.web.Application:
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/upload', UploadHandler)],
        static_path=os.path.join(os.path.dirname(f'{__file__}/../../'),
                                 'static'),
        template_path=os.path.join(os.path.dirname(f'{__file__}/../../'),
                                   'templates'))


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
