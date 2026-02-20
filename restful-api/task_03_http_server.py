#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path

        if path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!".encode())

        elif path == "/data":
            dataset = {"name": "John", "age": 30, "city": "New York"}
            body = json.dumps(dataset)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(body.encode())

        elif path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK".encode())

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found".encode())

server = HTTPServer(("localhost", 8000), Handler)
server.serve_forever()
