import mediapipe as mp
import cv2

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def detect_gesture(frame):
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(img_rgb)

    if result.pose_landmarks:
        left_hand = result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
        right_hand = result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
        head = result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE]

        # Se ambas as mãos estão acima da cabeça
        if left_hand.y < head.y and right_hand.y < head.y:
            return True

    return False
