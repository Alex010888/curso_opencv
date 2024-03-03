#GUARDAR UN VIDEO
import cv2

captura = cv2.VideoCapture(0)
# Para grabar un video necesitamos de la función cv2.VideoWriter, en ella especificamos el nombre del video con el que se guarda el video seguido de su extensión, el segundo argumento es el codec del video (si quieres más información puedes buscar en los docs de OpenCV). Como tercer argumento se indica el número de fps (frames per second / fotogramas por minuto), y finalmente se especifica el tamaño de los fotogramas (640,480), 640 pixeles de ancho y 480 de alto.
salida = cv2.VideoWriter('videoSalida.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))

while (captura.isOpened()):
  ret, imagen = captura.read()
  if ret == True:
    cv2.imshow('video', imagen)
    salida.write(imagen)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break
captura.release()
salida.release()
cv2.destroyAllWindows()