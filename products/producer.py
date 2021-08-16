import json
import pika

from admin.settings import MQTT_URL

params = pika.URLParameters(MQTT_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    print(f"Publish to {method} with the data: {body}")
    json_body = json.dumps(body)
    propreties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json_body, properties=propreties)
