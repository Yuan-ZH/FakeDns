import tornado
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./index.html")


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(80)
    tornado.ioloop.IOLoop.current().start()