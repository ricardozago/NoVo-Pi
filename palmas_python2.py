#install jsonrpclib with pip install jsonrpclib

import os
import jsonrpclib

def getServer():
    ip = os.environ.get('MOPIDYSERVER', '127.0.0.1:6680')
    return jsonrpclib.Server('http://{}/mopidy/rpc'.format(ip))

server = getServer()

if server.core.playback.get_state()=="playing":
    server.core.playback.pause()
else:
    server.core.playback.play()
