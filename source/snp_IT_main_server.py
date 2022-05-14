import tornado.ioloop
import tornado.web
import cv2


class MainHandler(tornado.web.RequestHandler):
    def get(self) -> None:
        self.render("../templates/main.html")


def make_app() -> tornado.web.Application:
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
