#Capturar, guardar y leer un video en OpenCV y Python
import cv2

# cv2.VideoCapture(0), la cual nos permitirá iniciar el proceso de captura del video.
capturar = cv2.VideoCapture(0)
# Aquí tenemos la estructura de repetición while, la cual será infinita mientras se esté capturando el video hasta que sea presionada una tecla como veremos a continuación.
while (capturar.isOpened()):
    #La función .read(), en este caso captura.read(), desempaqueta dos valores, el primero es una variable booleana, y el segundo la imagen en sí. A continuación brevemente las dos variables obtenidas en este programa:
    #ret: Esta variable booleana es True cuando SÍ se ha capturado una imagen, mientras que es False cuando NO se ha capturado una imagen con la cual trabajar.
    ret,imagen = capturar.read()
    #Este condicionante: if ret == True, nos permite seguir si es que existe una imagen capturada, también se podría comparar con False, y aplicar break, en caso que no se tenga la imagen.
    if ret == True:
        cv2.imshow('Video', imagen)
        #Este condicionante va a permitir salir del programa o terminar la visualización, hasta que sea presionada la tecla s. Se añade & 0xFF, cuando la máquina en la que se está realizando el programa es de 64 bits.
        # Si durante la ejecución del programa se ha presionado la tecla s, entonces se activa break, y sale del while.
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
        else: break
    capturar.release()
    cv2.destroyAllWindows()