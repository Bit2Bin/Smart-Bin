import cv2
from clarifai.rest import ClarifaiApp
import serial

stream = serial.Serial('COM7', baudrate=9600, timeout=1)
def servomove(result):
    print(result)
    if result == "recycle":
        stream.write(1)
        print("Its recycling")
    elif result == "compost":
        stream.write(2)
        print("Its Compost")
    else:
        stream.write(3)
        print("Its Garbagw")

def capture():
    result =""
    cap = cv2.VideoCapture(1)
    ret, frame = cap.read()
    cv2.imshow('image', frame)
    cv2.imwrite('Test.png', frame)
    cap.release()
    app = ClarifaiApp()
    model = app.models.get('waste')
    response = model.predict_by_filename('Test.png')
    concepts = response['outputs'][0]['data']['concepts']
    for concept in concepts:
        # print(concept['name'])
        result = concept['name']
        break
    cv2.destroyAllWindows()
    servomove(result)

while (True):
    data = str(stream.readline().decode("ascii"))
    print(data)
    for i in range(0,len(data)):
        if ord(data[i]) == ord("1"):
            capture()
