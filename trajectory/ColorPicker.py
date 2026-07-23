import cv2
from cvzone.ColorModule import ColorFinder
import func
video_path = (r"data\vid (3).mp4")
cap = cv2.VideoCapture(video_path)
myColorFinder = ColorFinder(True)
paused = False
frame = None
while True:
    if not paused:
        success, frame = cap.read()
        if not success:
            break
    if frame is not None:
        imgColor, mask = myColorFinder.update(frame)
        cv2.imshow("Video", func.resize(imgColor))

    key = cv2.waitKey(30) & 0xFF
    if key == ord('s'):
        paused = True
    elif key == ord('p'):
        paused = False
    elif key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
