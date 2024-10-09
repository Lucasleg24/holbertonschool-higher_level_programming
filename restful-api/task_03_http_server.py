#!/usr/bin/python3

import json
import http.server

"""
class for check the server with a little API
"""


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    """
    contain the def for functionnement of API
    """

    def do_GET(self):
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


PORT = 8000


with http.server.HTTPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()
