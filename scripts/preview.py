"""Serve the built portfolio without caching stale review pages."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse

class PreviewHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, max-age=0')
        super().end_headers()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=4176)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent / 'dist'
    server = ThreadingHTTPServer(('127.0.0.1', args.port), partial(PreviewHandler, directory=str(root)))
    print('Portfolio preview: http://127.0.0.1:%s/' % args.port, flush=True)
    server.serve_forever()
