import cv2
import pygame
import time
from deepface import DeepFace
import threading 

# Global variable to control whether emotion detection is paused or not
paused = False

def play_music(emotion):
    # Define a dictionary mapping emotions to music tracks
    emotion_music = {
        "happy": r"C:\Users\HP\Downloads\enjoy_59sec-191887.mp3",
        "sad": r"C:\Users\HP\Downloads\emotional-cinematic_34sec-186758.mp3",
        "angry": r"C:\Users\HP\Downloads\emotional-cinematic_34sec-186758.mp3",
        "surprised": r"C:\Users\HP\Downloads\happy-birthday-to-you-high-school-party-94107.mp3" ,
        "fear": r"C:\Users\HP\Downloads\Seniors_Malayalam_Movie_Drama_Theme_Music_By_Alphons_Jo_stbBIVgpxWA.mp3",
        "neutral": r"C:\Users\HP\Downloads\melancholy-ambient-always-be-with-me-184241.mp3",
        # Add more emotions and corresponding music tracks as needed
    }

    # Check if the detected emotion has a corresponding music track
    if emotion in emotion_music:
        track_path = emotion_music[emotion]
        print("Playing music for emotion:", emotion)
        print("Track path:", track_path)
        pygame.mixer.init()
        pygame.mixer.music.load(track_path)
        pygame.mixer.music.play()
        # Wait for the music to finish playing
        while pygame.mixer.music.get_busy():
            time.sleep(1)
        # Resume emotion detection after music finishes
        global paused
        paused = False

def toggle_pause():
    # Toggle the value of the paused variable
    global paused
    paused = not paused

def start_emotion_detection():
    global paused
    while True:
        if not paused:
            ret, frame = img.read()
            cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                face = frame[y:y + h, x:x + w]
                result = DeepFace.analyze(face, actions=['emotion'], enforce_detection=False)
                if isinstance(result, list) and result and 'dominant_emotion' in result[0]:
                    emotion = result[0]['dominant_emotion']
                    print("Detected emotion:", emotion)
                    if not paused:
                        play_music(emotion)  # Play music based on detected emotion

def emotions():
    global img
    img = cv2.VideoCapture(0)
    while True:
        ret, frame = img.read()
        cv2.imshow('frame', frame)
        # Check for key press events
        key = cv2.waitKey(1) & 0xFF
        if key == ord(' '):
            break
        elif key == ord('p'):
            toggle_pause()
        elif key == ord('s'):
            # Start emotion detection again
            global paused
            paused = False
            # Start emotion detection thread
            emotion_thread = threading.Thread(target=start_emotion_detection)
            emotion_thread.daemon = True
            emotion_thread.start()

    img.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    emotions()
