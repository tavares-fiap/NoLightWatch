import cv2
from gesture_detector import detect_gesture
from fall_detector import detect_fall
import pygame
import time

pygame.mixer.init()
ultimo_alerta = {}
cooldown_segundos = 3  # tempo mínimo entre alertas iguais

def emitir_alerta(mensagem, som_path=None, tipo="geral"):
    agora = time.time()
    ultimo = ultimo_alerta.get(tipo, 0)

    if agora - ultimo < cooldown_segundos:
        return  # Ignora alertas repetidos muito próximos
    

    ultimo_alerta[tipo] = agora
    print("[ALERTA] " + mensagem)

    if som_path:
        try:
            pygame.mixer.music.load(som_path)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Erro ao tocar som: {e}")

def analisar_video(fonte):
    cap = cv2.VideoCapture(fonte)

    if not cap.isOpened():
        print("Erro ao abrir a câmera ou vídeo.")
        return

    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1
        if frame_count % 3 != 0:
            continue  # Pula este frame, só processa 1 a cada 3

        # Processa gesto
        gesto_detectado = detect_gesture(frame)
        if gesto_detectado:
            emitir_alerta("Gesto de ajuda detectado!", "sounds/gesture.mp3", tipo="gesto")
            cv2.putText(
                frame,
                "PEDIDO DE AJUDA DETECTADO!",
                (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                1,
                (0, 0, 255),
                2
            )

        # Processa queda
        queda_detectada = detect_fall(frame)
        if queda_detectada:
            emitir_alerta("Queda detectada!", "sounds/fall.mp3", tipo="queda")
            cv2.putText(
                frame,
                "QUEDA DETECTADA!",
                (10, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                1,
                (0, 0, 255),
                2
            )

        cv2.imshow("Monitoramento", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # Tecla ESC para sair
            break

    cap.release()
    cv2.destroyAllWindows()
