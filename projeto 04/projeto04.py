import cv2
from cvzone.HandTrackingModule import HandDetector

# capturar a imagem da webcam
webcam = cv2.VideoCapture(0)

# configuração do rastreador de mãos
rastreador = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    # salvar em uma variável as imagens lidas da webcam
    sucesso, imagem = webcam.read()

    # inverter a imagem horizontalmente
    imagem2 = cv2.flip(imagem,1)

    # procurar as mãos no vídeo e # salvar em uma variável as coordenadas
    coordenadas, imagem_maos = rastreador.findHands(imagem2)

    # mostrar as coordenadas no terminal
    print(coordenadas)

    # mostrar o vídeo em uma janela
    cv2.imshow("projeto 04 - IA", imagem2)

    # manter a janela aberta até pressionar qualquer tecla
    if cv2.waitKey(1) != -1:
        break

# liberar a webcam e destruir todas as janelas de vídeo
webcam.release()
cv2.destroyAllWindows()