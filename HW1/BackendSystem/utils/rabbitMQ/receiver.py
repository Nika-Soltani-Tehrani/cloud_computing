import os
import pika
import sys
from BackendSystem.utils.rabbitMQ.config import AMQP_URL
from BackendSystem.receive_system import ReceiveSystem


def main():
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()
    channel.queue_declare(queue='message')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        receive_system = ReceiveSystem()
        receive_system.execute(int(body))

    channel.basic_consume(queue='message', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
