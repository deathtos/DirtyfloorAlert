import socket
import os
from azure.storage.blob import BlockBlobStorage
from azure.storage.blob import BlobServiceClient, BlobClient
from azure.storage.blob import ContentSettings, ContainerClient
from time import sleep
from time import time

def setupBlobService(account_name, account_key):
	bbs = BlockBlobService(
		account_name = account_name,
		account_key = account_key
	)
	return bbs

def sendPicsToBlob(path, dir_name, container_name, acount_name, account_key):
	print("Setting up Azure Blob Service")
	bbs = setupBlobService(account_name,account_key)
	print("Azure Blob Service initialized")
	print("Retrieving files to send to ABS")
	for file_name in os.listdir(path):
		blob_name = f"{dir_name}/{file_name}"
		file_path = f"{path}/{file_name}"
		bbs.create_blob_from_path(container_name,blob_name,file_path)

def setupBlobServiceCS(connectionstring):
    bbs = BlobServiceClient.from_connection_string(connectionstring)
    return bbs

def sendPicToBlobCS(connectionstring,container_name,file_name,path):
    bbs = setupBlobServiceCS(connectionstring)
    bbs_client = bbs.get_blob_client(container = container_name, blob = file_name)
    file_path = os.path.join(path,file_name)
    content_setting = ContentSettings(content_type = 'image/jpeg')
    print(f"uploading file - {file_name}")
    print(f"from path - {file_path}")
    with open(file_path, "rb") as data:
        bbs_client.upload_blob(data,overwrite=True,content_settings=content_setting)
	











#Old
#
#def setupSocket():
#    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    s.connect((host, port))
#    return s
#
#def sendPic(s, filePath):
#    print(filePath)
#    pic = open(filePath, 'rb')
#    chunk = pic.read(1024)
#    s.send(str.encode("STORE " + filePath))
#    t = time()
#    while chunk:
#        print("Sending Picture")
#        s.send(chunk)
#        chunk = pic.read(1024)
#    pic.close()
#    print("Done sending")
#    print("Elapsed time = " + str(time() - t) + 's')
#    s.close()
#    return "Done sending"
#
#def sendReceive(s, message):
#    s.send(str.encode(message))
#    reply = s.recv(1024)
#    print("We have received a reply")
#    print("Send closing message.")
#    s.send(str.encode("EXIT"))
#    s.close()
#    reply = reply.decode('utf-8')
#    return reply
#
#def transmit(message):
#    s = setupSocket()
#    response = sendReceive(s, message)
#    return response
#
#def backup(filePath):
#    s = setupSocket()
#    response = sendPic(s, filePath)
#    return response