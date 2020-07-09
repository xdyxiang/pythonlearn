from socketIO_client import SocketIO, LoggingNamespace

def on_bbb_response(*args):
    print('on_bbb_response', args)
    print("wo tao ni hou zi!!!!")

def on_connect():
    print('connect')

def on_disconnect():
    print('disconnect')

def on_reconnect():
    print('reconnect')




socketIO = SocketIO('127.0.0.1', 5000, LoggingNamespace)
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('reconnect', on_reconnect)


def on_myresponse(msg):
    print(msg)

def my_pong():
    print("wodiao!")


# Listen
socketIO.on("my_response",on_myresponse)
socketIO.on("my_pong",my_pong)
# send
socketIO.emit('my_ping', on_bbb_response)
socketIO.emit('my event',{"a":"bbb"})
socketIO.emit('my event1',"123","333333","456")
socketIO.wait(seconds=1)
# socketIO.wait()
