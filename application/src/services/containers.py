from typing import Dict
from services.storage_account import StorageAccount

class BlobContainer(StorageAccount):
    def __init__(self, container_name: str, account_name: str, service_principal: Dict) -> None:
        super().__init__(account_name, service_principal)
        print(f'initiating container {container_name} in account {account_name}')

    def upload(self, file):
        print('Uploading blob')
        print('...')
        print('Upload completed successfully')

    def download(self, file):
        print('Downloading blob')
        print('...')
        print('Download completed successfully')



class DataLakeContainer(StorageAccount):
    '''
    Class to use Data Lake as a file directory
    '''
    def __init__(self, container_name: str, account_name: str, service_principal: Dict) -> None:
        super().__init__(account_name, service_principal)
        print(f'initiating container {container_name} in account {account_name}')

    def upload(self, file):
        print('upload file to data lake')

    def download(self, file):
        print('Downloading file from data lake')