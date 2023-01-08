from typing import Dict

class StorageAccount:
    '''
    Class to interact with Azure storage account
    '''
    def __init__(self, name: str, service_principal: Dict) -> None:
        print(f'initializing storage account {name}')
        self.service_principal = service_principal
        self.account_name = name
        self.authenticate


    def authenticate(self):
        print(f"Authenticating using service principal")

    