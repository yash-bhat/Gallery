# amqps://ekydiwgu:NaoMzihFGBG7nzzzs5fXYh8HY6im6OPz@orangutan.rmq.cloudamqp.com/ekydiwgu

import pika

params = pika.URLParameters('amqps://ekydiwgu:NaoMzihFGBG7nzzzs5fXYh8HY6im6OPz@orangutan.rmq.cloudamqp.com/ekydiwgu')

# create connection with rabbitMQ
connection = pika.BlockingConnection(params)

# create channel
channel = connection.channel()

# publish
def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')