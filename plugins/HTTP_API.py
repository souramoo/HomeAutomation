import string,cgi,time
import subprocess
import threading
from Sensor import Sensor
import Driver
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            bits = string.split(self.path, "/")
            if len(bits) > 3:
                id = bits[1]
                param = bits[2]
                value = bits[3]
                for f in Driver.Drivers:
                    if f[0] == int(id):
                        f[1].setParameter(param, value)
                        self.send_response(200)
                        self.send_header('Content-type',    'text/html')
                        self.end_headers()
                        self.wfile.write("OK")
                        return
            self.send_response(200)
            self.send_header('Content-type',	'text/html')
            self.end_headers()
            self.wfile.write("Error")
            return
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

    def do_POST(self):
        return

class APIThread(threading.Thread):
    def run(self):
        try:
            server = HTTPServer(('', 8090), MyHandler)
            print 'started httpserver...'
            server.serve_forever()
        except KeyboardInterrupt:
            print '^C received, shutting down server'
            server.socket.close()

class HTTP_API(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        APIThread().start()
