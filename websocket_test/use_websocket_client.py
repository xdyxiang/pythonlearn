from websocket import create_connection
ws = create_connection("ws://10.1.5.18:5678")
print("Sending 'Hello, World'...")
ws.send("Hello, World")
result =  ws.recv()
print("Received '%s'" % result)
ws.send("admin:123456")
print("Sent admin")
result =  ws.recv()
print("Received '%s'" % result)
ws.send("我 是 谁？")
print("Sent 我是谁")
result =  ws.recv()
print("Received '%s'" % result)
ws.send("你是个都比！")
result =  ws.recv()
print("Received '%s'" % result)
ws.close()

