import http.server
import socketserver
from urllib.parse import parse_qs, urlparse

# Define valid credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Parse form data
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_data = parse_qs(post_data.decode('utf-8'))

        username = post_data.get('username', [''])[0]
        password = post_data.get('password', [''])[0]

        # Validate credentials
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            message = "Login successful!"
        else:
            message = "Invalid username or password"

        # Redirect to the HTML page with the message
        self.send_response(302)
        self.send_header('Location', f'/login.html?message={message}')
        self.end_headers()

    def do_GET(self):
        if self.path == '/login':
            self.path = '/login.html'
        return super().do_GET()

# Set up and run the server
PORT = 8000
Handler = RequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
