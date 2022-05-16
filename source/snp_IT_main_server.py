import tornado.ioloop
import tornado.web
import os
import cv2


class MainHandler(tornado.web.RequestHandler):
    def get(self) -> None:
        self.render("main.html", )


def make_app() -> tornado.web.Application:
    return tornado.web.Application([
        (r'/', MainHandler)],
        static_path=os.path.join(os.path.dirname(f'{__file__}/../../'),
                                 'static'),
        template_path=os.path.join(os.path.dirname(f'{__file__}/../../'),
                                   'templates'))


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
