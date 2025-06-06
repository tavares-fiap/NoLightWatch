import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def detect_fall(frame):
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(img_rgb)

    if not result.pose_landmarks:
        return False
    mp_drawing.draw_landmarks(
        frame,
        result.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2),
        connection_drawing_spec=mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2)
    )
    landmarks = result.pose_landmarks.landmark
    left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
    right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]
    left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP]
    right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP]
    # Calcular médias das posições normalizadas (valores entre 0 e 1)
    shoulder_y = (left_shoulder.y + right_shoulder.y) / 2 # Média da altura dos ombros (eixo Y)
    hip_y = (left_hip.y + right_hip.y) / 2 # Média da altura dos quadris (eixo Y)
    x_shoulder = (left_shoulder.x + right_shoulder.x) / 2 # Média da posição horizontal dos ombros (eixo X)
    y_media = (shoulder_y + hip_y) / 2 # Altura média do tronco (ponto entre ombros e quadris)
    # Obter tamanho da imagem em pixels
    altura, largura = frame.shape[:2]
    # Converter coordenadas normalizadas (0 a 1) para coordenadas de pixel na imagem
    ponto_x = int(x_shoulder * largura)
    ponto_y = int(y_media * altura)
    LIMIAR_ALTURA_QUEDA = 0.50
    # Linha de referência (em pixels) para detectar se o corpo está "perto do chão"
    linha_limite_y = int(LIMIAR_ALTURA_QUEDA * altura)
    # Desenhar o ponto médio do tronco (em azul)
    cv2.circle(frame, (ponto_x, ponto_y), 8, (255, 0, 0), -1)
    # Desenhar linha horizontal vermelha na altura de 50% da imagem
    cv2.line(frame, (0, linha_limite_y), (largura, linha_limite_y), (0, 0, 255), 2)

    # Heurísticas:
    # 1. Está perto do chão? (tronco abaixo da metade da imagem(valor tem que ser adaptado dependendo da posicao da camera))
    perto_do_chao = y_media > LIMIAR_ALTURA_QUEDA

    # 2. Está em posição horizontal? (ombros e quadris quase na mesma altura vertical)
    posicao_horizontal = abs(shoulder_y - hip_y) < 0.1

    if perto_do_chao and posicao_horizontal:
        return True

    return False
