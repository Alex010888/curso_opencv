#CONSTRUYENDO UNA IMAGEN CON NUMPY
import cv2
import numpy as np

bgr = np.zeros((300, 300, 3), dtype=np.uint8)
cv2.imshow('BGR', bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()