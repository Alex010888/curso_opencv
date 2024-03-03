#LEER UN VIDEO
import cv2

#En vez de especificar el número de cámara que se utilizaba en el caso de realizar un video streaming, aquí lo que se hace es simplemente especificar entre comillas el nombre del video junto a su extensión. Recuerda que si el video está en una localización diferente a de tu programa, será necesario indicar toda la dirección.
captura = cv2.VideoCapture('videoSalida.avi')
while (captura.isOpened()):
  ret, imagen = captura.read()
  if ret == True:
    cv2.imshow('video', imagen)
    # Pudiste haber notado que en cv2.waitKey, se especificó 30 y no 1 como hemos visto hasta el momento. Con 30 el video se aprecia mejor con respecto a la velocidad del mismo. Por el contrario con 1, puede que tu video pase considerablemente rápido, esto es debido a que OpenCV quiere realizar el proceso lo más rápido posible sin importar el fps original del video.
    if cv2.waitKey(30) == ord('s'):
      break
  else: break
captura.release()
cv2.destroyAllWindows()s