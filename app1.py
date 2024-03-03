#Leer una imagen
#Visualizar una imagen
#Guardar/Almacenar una imagen
import cv2
imagen = cv2.imread('logo.png') 
cv2.imshow('Logo OpenCV',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
