# amqps://ekydiwgu:NaoMzihFGBG7nzzzs5fXYh8HY6im6OPz@orangutan.rmq.cloudamqp.com/ekydiwgu

import pika

params = pika.URLParameters('amqps://ekydiwgu:NaoMzihFGBG7nzzzs5fXYh8HY6im6OPz@orangutan.rmq.cloudamqp.com/ekydiwgu')

# create connection with rabbitMQ
connection = pika.BlockingConnection(params)

# create channel
channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started consuming')

channel.start_consuming()

channel.close()
