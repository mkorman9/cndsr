import http.server

if __name__ == '__main__':
    http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=8080)
