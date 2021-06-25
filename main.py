import cv2

def webcam_smile():
    cap = cv2.VideoCapture(0)

    while (True):
        ret, frame = cap.read()
        smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")
        smiles = smile_cascade.detectMultiScale(frame, scaleFactor=1.8, minNeighbors=20)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(frame, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 3)
        cv2.imshow('webcam', frame)

        if  cv2.waitKey(1) & 0XFF == ord('q'):
            break

    cap.release()
    # out.release()
    cv2.destroyAllWindows()



def picture_smile():
    img = cv2.imread('./pictures/smile_1.jpg')
    smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")
    smiles = smile_cascade.detectMultiScale(img, scaleFactor=1.8, minNeighbors=20)

    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(img, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 3)

    cv2.imshow("smile detected", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # picture_smile()
    webcam_smile()