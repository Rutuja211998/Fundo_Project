"""
This file contains server file to run the server.
Author: Rutuja Tikhile
Date:24/3/2020
"""
from http.server import HTTPServer
from routes import Server


def run(server_class=HTTPServer, handler_class=Server, addr="127.0.0.1", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run(HTTPServer, Server)