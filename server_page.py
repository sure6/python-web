# coding=utf-8
"""
date: 2021/7/11 13:01
author: lee sure
"""
import http.server
import socketserver
import urllib.parse

# BaseHTTPHTTPRequestHandler
# SimpleHTTPRequestHandler

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self): # override super.do_GET
        print("self.path: "+self.path)
        parsedParams = urllib.parse.urlparse(self.path)
        print("parsedParams: " + parsedParams.query)
        queryParsed = urllib.parse.parse_qs(parsedParams.query)
        print("queryParsed: "+str(queryParsed))
        if parsedParams.path == "/test":
            self.processMyRequest(queryParsed)
        else:
            # Default to serve up a local file
            http.server.SimpleHTTPRequestHandler.do_GET(self);

    def processMyRequest(self, query):

        self.send_response(200)
        # self.send_header('Content-Type', 'text/json; charset=utf-8')
        self.end_headers()

        print(query.get('user'))
        # self.wfile.write("<sample>Some XML</sample>");
        # self.wfile.close();

PORT = 8000

Handler = MyHandler

with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()