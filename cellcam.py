#Acesso a camera do smartphone utilizando opencv

import cv2



video = cv2.VideoCapture()

#colocar o ip e porta gerado pelo app entre as aspas, exemplo http://192.168.1.1:4742/ aplicativo sugerido: Droidcam

ip = " " 



video.open(ip)



while True:
    check, img = video.read()
    cv2.imshow('img', img)
    key = cv2.waitKey(1)
    if key == ord('q'):  
        break

video.release()


cv2.destroyAllWindows()

