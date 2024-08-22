import cv2

# Inicializa la cámara (0 generalmente es la cámara predeterminada)
cam = cv2.VideoCapture(0)

# Lee la imagen desde la cámara
ret, frame = cam.read()

# Verifica si la cámara se abrió correctamente
if not ret:
    print("No se pudo acceder a la cámara")
else:
    # Muestra la imagen capturada en una ventana
    cv2.imshow('Imagen capturada', frame)

    # Guarda la imagen capturada
    cv2.imwrite('foto_capturada.jpg', frame)

    # Espera a que el usuario presione una tecla para cerrar la ventana
    cv2.waitKey(0)

# Libera la cámara y cierra la ventana
cam.release()
cv2.destroyAllWindows()