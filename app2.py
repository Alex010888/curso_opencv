#Guardar/Almacenar una imagen
import cv2
#imagen = cv2.imread('logo.png',0) .La imagen será leída en escala de grises.
imagen = cv2.imread('logo.png',0)
cv2.imwrite('Grises.png',imagen)
cv2.imshow('Logo Opencv Grises',imagen)
#cv2.waitKey(0), la imagen se visualiza infinitamente, hasta que presiones cualquier tecla.
cv2.waitKey(0)
cv2.destroyAllWindows()
