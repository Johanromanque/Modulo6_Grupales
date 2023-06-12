import http.server
import socketserver

puerto=5000
handler= http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",puerto),handler) as servidor:
    print (f"Bienvenidos a TeLoVendo {puerto} ")
    servidor.serve_forever()
