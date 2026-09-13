from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Python Automated CI/CD Pipeline!")

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 5000), SimpleHandler)
    print("NOW Server running on port 5000...")
    server.serve_forever()
