from http.server import BaseHTTPRequestHandler, HTTPServer

page = """<h1>Food ordering login</h1>
<input id="username" placeholder="Name">
<input id="password" type="password" placeholder="Password">
<button id="login" onclick="checkLogin()">Log in</button>
<p id="message"></p>
<script>
function checkLogin() {
  let name = document.getElementById('username').value;
  let password = document.getElementById('password').value;
  let result = name === 'student' && password === 'pizza123';
  document.getElementById('message').textContent = result ? 'Welcome!' : 'Login failed';
}
</script>"""

class LoginPage(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(page.encode())

if __name__ == "__main__":
    print("Open http://127.0.0.1:8000")
    HTTPServer(("127.0.0.1", 8000), LoginPage).serve_forever()
