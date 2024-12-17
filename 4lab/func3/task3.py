import cv2
from sys import argv
from pathlib import Path

def main():
    if len(argv) != 2:
        print('error! enter a path to your file')
    path = Path(argv[1])

    video = cv2.VideoCapture(path)
    if not video.isOpened():
        print('error! No such video file')
        exit()
    while True:
        ret, frame = video.read()
        if not ret:
            break
        cv2.putText(frame, str(video.get(cv2.CAP_PROP_FPS)), (25, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
        cv2.putText(frame, str(argv[1]), (25, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

main()