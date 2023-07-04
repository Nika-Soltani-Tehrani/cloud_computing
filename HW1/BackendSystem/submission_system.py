from BackendSystem.utils.S3.s3 import S3
from BackendSystem.utils.ImageProcessing.image_proccessing import ImageProcessing
from BackendSystem.utils.DBaaS.database import Database
from PIL import Image
import requests
from io import BytesIO
import pika
from BackendSystem.utils.rabbitMQ.config import AMQP_URL


class SubmissionSystem:

    def __init__(self):
        self.s3 = S3()
        self.image_processing = ImageProcessing()
        self.database = Database()
        # print("in init")
        self.id_generator = 12346
        # print("in init")

    @staticmethod
    def download_image(url):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img

    @staticmethod
    def send_message(user_id):
        connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
        channel = connection.channel()

        channel.queue_declare(queue='message')

        channel.basic_publish(exchange='', routing_key='message', body=user_id)
        print(f" Your post with id {user_id} submitted successfully.")
        connection.close()

    def execute(self, description, photo_url, email_address):
        self.id_generator = str(self.id_generator + 1)
        # print("in init")
        initial_state = 'processing'
        initial_category = 'not recognized'
        # print("in init")
        self.database.insert_data(self.id_generator, description, email_address, initial_state, initial_category)
        self.send_message(self.id_generator)


ss = SubmissionSystem()
ss.execute("testing system", "world", "nsoltanitehrani@gmail.com")
