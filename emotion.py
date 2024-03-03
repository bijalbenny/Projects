
import cv2
from deepface import DeepFace
def emotions():

    img = cv2.VideoCapture(0)

    while True:
        ret, frame = img.read()
        cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            result = DeepFace.analyze(face, actions=['emotion'], enforce_detection=False)
            if isinstance(result, list) and result and 'dominant_emotion' in result[0] :
                emotion = result[0]['dominant_emotion']
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(frame, f'Analysis: {emotion}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    img.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    emotions()
