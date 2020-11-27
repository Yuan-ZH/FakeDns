import tornado
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def prepare(self):
        if self.request.protocol == "http":
            self.redirect("https://%s" % self.request.full_url()
            [len("http://"):], permanent=True)
    def get(self):
        self.render("./index.html")




application = tornado.web.Application([
    (r"/", MainHandler),
])
http_server = tornado.httpserver.HTTPServer(application,
                                            ssl_options={

                                                "certfile": os.path.join("https_svr_key2.pem"),
                                                "keyfile": os.path.join("https_svr_key1.pem"),
                                            }
                                            )
if __name__ == '__main__':
    http_server.listen(443)
    tornado.ioloop.IOLoop.instance().start()