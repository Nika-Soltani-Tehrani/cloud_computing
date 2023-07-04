import pika
from BackendSystem.utils.rabbitMQ.config import AMQP_URL


def send_message(user_id):
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()

    channel.queue_declare(queue='message')

    channel.basic_publish(exchange='', routing_key='message', body=user_id)
    # print(f" [{user_id}] Sent {message}")
    connection.close()


inter = input('enter a message')
send_message('123')
