from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        
        # Set response headers
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        
        # Write response body
        self.wfile.write(b"Hello, this is a simple API!")
        self.send_header("Content-type", "application/json")

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
