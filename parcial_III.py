from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import crud_producto
port = 3002

crud_producto = crud_producto.crud_producto()
class servidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path = "menu.html"
            return SimpleHTTPRequestHandler.do_GET(self)
            
        if self.path=="/crud_producto":
            len = int(self.headers["Content-Length"])
            data = self.rfile.read(len)
            data = data.decode()
            data = parse.unquote(data)
            data = json.loads(data)

            resp = crud_producto.consultar(data)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(resp).encode())

    def do_POST(self):
        lenc = int(self.headers["Content-Length"])
        data = self.rfile.read(lenc)
        data = data.decode()
        data = parse.unquote(data)
        data = json.loads(data)
        if self.path=="/crud_producto":
            resp = crud_producto.administrar_productos(data)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(str(resp).encode())

print("Server iniciado en el puerto ", port)
server = HTTPServer(("localhost", port), servidorBasico)
server.serve_forever()