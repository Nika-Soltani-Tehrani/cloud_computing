import BackendSystem.utils.S3.config as config
import boto3
import logging


class S3:

    def __init__(self):
        self.domain = config.DOMAIN
        self.bucket_name = config.BUCKETNAME
        self.access_key = config.ACCESSKEY
        self.secret_key = config.SECRETKEY
        self.bucket = self.connect()

    def connect(self):
        try:
            s3_resource = boto3.resource(
                's3',
                endpoint_url=self.domain,
                aws_access_key_id=self.access_key,
                aws_secret_access_key=self.secret_key
            )
            return s3_resource
        except Exception as exc:
            logging.info(exc)
        else:
            bucket = s3_resource.Bucket(self.bucket_name)
            return bucket

    def get_bucket_files(self):
        for obj in self.bucket.objects.all():
            logging.info(f"object_name: {obj.key}, last_modified: {obj.last_modified}")

    def upload_file(self, file_name):
        file_path = f'./{file_name}.png'
        object_name = f'{file_name}.png'
        with open(file_path, "rb") as file:
            self.bucket.put_object(
                ACL='private',
                Body=file,
                Key=object_name
            )

    def get_file(self, image_name):
        object_name = f'{image_name}.png'
        download_path = f'{image_name}-downloaded.png'
        self.bucket.download_file(
            object_name,
            download_path
        )

    def remove_image(self, image_name):
        object_name = f'{image_name}.png'
        img_object = self.bucket.Object(object_name)
        img_object.delete()
