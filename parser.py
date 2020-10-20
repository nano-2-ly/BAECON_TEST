import requests
import json
import cv2
import numpy as np
from PIL import Image

url = "http://192.168.35.29:80/capture"
# url = "http://54.180.24.62:8000/device/P2"


# data = {'command' : 'C000'}
# response =  requests.post(url, data=json.dumps(data))

response =  requests.get(url)

encoded_img  = np.fromstring(response.content, dtype = np.uint8)
img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
im = Image.fromarray(img)
im.save("your_file.jpeg")
print(img.shape)

print("status code : ", response.content)