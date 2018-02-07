import http.server


def run():
    http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=8080)
