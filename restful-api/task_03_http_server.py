#!/usr/bin/python3
"""
import from http.server build an HTTP API
import json to convert answers
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MyHandler(BaseHTTPRequestHandler):
    """
    class inherits from BaseHTTPRequestHandler
    adapting handler behaviour
    """
    def do_GET(self):
        """
        Running GET request and sending the right response
        depending on the endpoint
        """
        path = self.path

        if path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())

        elif path == "/data":
            dataset = {"name": "John", "age": 30, "city": "New York"}
            body = json.dumps(dataset)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body.encode())

        elif path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode())

        elif path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
                }
            info_json = json.dumps(info)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(info_json.encode())

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode())


server = HTTPServer(("localhost", 8000), Handler)
server.serve_forever()
