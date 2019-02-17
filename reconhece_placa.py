import os, cv2, mahotas, pytesseract, time 
from PIL import Image
import re

camera = cv2.VideoCapture(0)
regex = re.compile(r'(\S{3}\-\d{4})')
while True:
    (sucesso, frame) = camera.read()
    if not sucesso:
        break 
    imgC = frame
    cv2.imshow("Encontrando placas...", frame)

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("imagem_frame.jpg", img)
           
    caracs = pytesseract.image_to_string(Image.open("imagem_frame.jpg"))
    placa = regex.findall(caracs)
    if(len(placa) > 0):
        print(placa[0])
    if cv2.waitKey(1) & 0xFF == ord("s"):
        break
camera.release()
cv2.destroyAllWindows()