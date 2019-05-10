import requests
import datetime
import cv2


#http://benalexkeen.com/using-azure-cognitive-services-to-caption-video/
#88726c45c82248f3816bcc223ea56ab8
#https://mosellandwerkstaetten.de/shop/media/image/4d/68/c9/untersetzer-tasse-loeffel.jpg

#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

subscription_key = "" # your subscription key here
vision_tag_url = "https://westeurope.api.cognitive.microsoft.com/vision/v1.0/tag"

headers  = {'Content-Type': 'application/json',
                'Ocp-Apim-Subscription-Key': subscription_key }
# Make a request to the Azure Cognitive Services Vision Analysis API
try:
    response = requests.post(vision_tag_url,
            headers=headers,
            data="""{   "url": "https://mosellandwerkstaetten.de/shop/media/image/4d/68/c9/untersetzer-tasse-loeffel.jpg" }""")
        # Extract the json from the response
    tags = response.json()
    print(tags)
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


