"""
Flask application that serves as a direct replacement for the original Node.js
HTTP server (server.js). Faithfully replicates the exact behavior: returns
HTTP 200 with Content-Type text/plain and body 'Hello, World!\n' for every
request, regardless of HTTP method or URL path.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
def catch_all(path):
    """Handle all incoming HTTP requests with an identical static response.

    This replicates the original Node.js server behavior where the request
    handler callback ignores the request object entirely — all HTTP methods
    and all URL paths receive the same response.

    Args:
        path: The URL path captured by Flask's routing. Accepted but
              intentionally ignored to match the original server's behavior.

    Returns:
        A Flask response tuple containing:
        - Body: 'Hello, World!\\n' (14 bytes including trailing newline)
        - Status code: 200
        - Headers: Content-Type set to 'text/plain'
    """
    return 'Hello, World!\n', 200, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
