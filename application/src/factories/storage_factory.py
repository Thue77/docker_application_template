from services.containers import BlobContainer, DataLakeContainer
from typing import Protocol, Dict

class Container(Protocol):
    container_name: str
    account_name: str
    service_principal: Dict

    def upload():
        ...
    
    def download():
        ...


def test(c: Container):
    c.download('file')

def Factory(type ="Blob") -> Container:
 
    """Factory Method"""
    container_types = {
        "Blob": BlobContainer,
        "Data lake": DataLakeContainer
    }
 
    return container_types[type]