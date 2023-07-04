import requests
import BackendSystem.utils.ImageProcessing.config as config


class ImageProcessing:
    def __init__(self):
        self.api_key = config.API_KEY
        self.api_secret = config.API_SECRET

    def get_most_probable_tag(self, image_url):
        response = requests.get(
            'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
            auth=(self.api_key, self.api_secret))
        tags = response.json()['result']['tags']
        tag_name_list = []
        for tag in tags:
            confidence = tag['confidence']
            tag_name = tag['tag']['en']
            tag_name_list.append(tag_name)
            # print(f'Confidence: {confidence}, tag: {tag_name}')

        return str(tag_name_list[0])


# ip = ImageProcessing()
# bicycle_url_r1 = 'https://nikast.s3.ir-thr-at1.arvanstorage.com/bike.png'
# car_url_r1 = 'https://nikast.s3.ir-thr-at1.arvanstorage.com/car.png'
# motor_url_r1 = 'https://nikast.s3.ir-thr-at1.arvanstorage.com/motor.png'
# panda_url_r1 = 'https://nikast.s3.ir-thr-at1.arvanstorage.com/panda.png'
# print(ip.get_most_probable_tag(motor_url_r1))
