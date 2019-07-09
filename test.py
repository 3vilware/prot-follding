import webbrowser
url = 'http://localhost:63342/viewer.html?' + '6fxa.pdb' 


# HTTP Server needed depending wich OS is the command
    # Windows: python -m http.server 63342
    # Linux: python -m SimpleHttpServer 63342

import SimpleHTTPServer
import SocketServer

PORT = 63342

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(url)

httpd.serve_forever()
