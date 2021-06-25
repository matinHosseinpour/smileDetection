import cv2

def webcam_smile():
    cap = cv2.VideoCapture(0)

    while (True):
        ret, frame = cap.read()
        frame = detect(frame)
        cv2.imshow('webcam', frame)

        if  cv2.waitKey(1) & 0XFF == ord('q'):
            break

    cap.release()
    # out.release()
    cv2.destroyAllWindows()



def picture_smile():
    img = cv2.imread('./pictures/smile_1.jpg')
    img = detect(img)
    cv2.imshow("smile detected", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def detect(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    smiles = smile_cascade.detectMultiScale(frame, scaleFactor=1.8, minNeighbors=20)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
    return frame


if __name__ == '__main__':
    picture_smile()
    # webcam_smile()