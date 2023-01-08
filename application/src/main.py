import tkinter as tk
from factories.storage_factory import Factory, Container
# from services.containers import DataLakeContainer

def moving_files(container: Container):
    container.upload('file')
    container.download('file')

def main():
    type = 'Data lake'
    # type = 'Blob'
    container = Factory(type)("container_namer","account","sp")

    moving_files(container)

    # container.download("file")


if __name__ == "__main__":
    print('running main')
    main()