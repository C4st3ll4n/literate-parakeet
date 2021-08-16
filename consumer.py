import pika
from decouple import config

url = config('MQTT_URL')
params = pika.URLParameters(url)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print("Received in admin app at admin queue")
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)
print("Started consuming")

channel.start_consuming()
channel.close()
