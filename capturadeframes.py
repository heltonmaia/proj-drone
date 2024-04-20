#script para fazer a captura de frames utilizando a camera do celular

import cv2
import os

video = cv2.VideoCapture()

#colocar o ip e porta gerado pelo app entre as aspas, exemplo http://192.168.1.1:4742/ , aplicativo sugerido: Droidcam

ip = "http://192.168.1.7:4747/video"

video.open(ip)

#setando a resolução em 640x480
video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

frame_count = 0
output_folder = "captured_frames"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

while True:
    check, img = video.read()
    
    #contagem de frames
    cv2.putText(img, f"Frames: {frame_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('img', img)
    if frame_count % 10 == 0:  #capturando 1 a cada 5 frames, para ter mais tempo para tirar as fotos
        cv2.imwrite(os.path.join(output_folder, f"frame_{frame_count}.jpg"), img)
    key = cv2.waitKey(1)
    if key == ord('q'):  #se q for pressionada, já finaliza tudo
        break
    frame_count += 1

video.release()
cv2.destroyAllWindows()
