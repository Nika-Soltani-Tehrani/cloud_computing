from BackendSystem.utils.S3.s3 import S3
from BackendSystem.utils.ImageProcessing.image_proccessing import ImageProcessing
from BackendSystem.utils.EmailService.email_service import send_email
from BackendSystem.utils.DBaaS.database import Database
from PIL import Image
import requests
from io import BytesIO


class ReceiveSystem:

    def __init__(self):
        self.s3 = S3()
        self.image_processing = ImageProcessing()
        self.database = Database()
        self.accepted_category = ['bicycle', 'car', 'motor cycle', 'bike']

    @staticmethod
    def download_image(url):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img

    def execute(self, post_id):
        flag = 0
        post_tuple = self.database.get_data(post_id)
        post_list = list(post_tuple)
        if post_list[3] == 'processing':
            print('Your post has not yet been configured')
            image_name = str(post_id) + '.png'
            # image_url = self.s3.get_file(image_name)
            # image_url = f'https://nikast.s3.ir-thr-at1.arvanstorage.com/{image_name}'
            image_url = 'https://nikast.s3.ir-thr-at1.arvanstorage.com/motor.png'
            result = self.image_processing.get_most_probable_tag(image_url)
            print("result= " + result)
            for category in self.accepted_category:
                if category in result:
                    print('category= ' + category)
                    self.database.update_category(post_id, category)
                    self.database.update_state(post_id, 'accepted')
                    send_email(post_list[2], post_id, True)
                    flag = 1
            if flag != 1:
                self.database.update_state(post_id, 'rejected')
                send_email(post_list[2], post_id, False)
