from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='172.18.105.45:9092')  # 连接kafka

# msg = "Hello World".encode('utf-8')  # 发送内容,必须是bytes类型
msg_dict = {
    "sleep_time": 10,
    "db_config": {
        "database": "test_1",
        "host": "xxxx",
        "user": "root",
        "password": "root"
    },
    "table": "msg",
    "msg": "Hello World"
}
msg = json.dumps(msg_dict).encode('utf-8')
producer.send('test1', msg)  # 发送的topic为test
producer.close()



# from kafka import KafkaConsumer

# consumer = KafkaConsumer('test', bootstrap_servers=['192.168.0.121:9092'])
# for msg in consumer:
#     recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
#     print(recv)