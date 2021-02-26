
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import ContainerClient

AZURE_STORAGE_ACCOUNT_NAME = 'imageuploadcode'
AZURE_STORAGE_ACCESS_KEY = 'sosQtC8gjpPgrxIkRfd+H3PWiYgHtktbzbfsFD6OwOwywq1OvykcHm2s+pc9RuOIvWFUb8mTooKQBKcifWuUKA=='

url = "https://{}.blob.core.windows.net".format(AZURE_STORAGE_ACCOUNT_NAME)

blob_service_client = BlobServiceClient(account_url= url, credential= AZURE_STORAGE_ACCESS_KEY)

account_info = blob_service_client.get_account_information()

container_client = blob_service_client.get_container_client('images')

container_list = blob_service_client.list_containers()

for container in container_list:
    print (container)

container_info = container_client.get_container_properties()

blob_list = container_client.list_blobs()

# for blob in blob_list:
#     print (blob)

# print (container_info)
