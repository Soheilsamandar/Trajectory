import cv2 as cv
import numpy as np
import os
import csv
import matplotlib.pyplot as plt
from func import resize, remove_file, create_mask, combined, append_to_file, show_plot

lower = np.array([0, 162, 0])
upper = np.array([16, 255, 255])

trajectory = []
frame_count = 0
prev_cX, prev_cY = 0, 0
prev_speed = 0
first_frame = True

output_dir = "analysis"
FILE_NAME = os.path.join(output_dir, "trajectory.csv")

remove_file(FILE_NAME)

with open(FILE_NAME, "w", newline="") as f:
    writer = csv.writer(f)
    headers = ["FRAME", "X", "Y", "SPEED", "ACCELERATION"]
    writer.writerow(headers)

vid_path = r"data\vid (2).mp4"
cap = cv.VideoCapture(vid_path)
while True:
    ret, frame = cap.read()
    if ret is False:
        break
    mask = create_mask(frame, lower, upper)
    res_msk = cv.bitwise_and(frame, frame, mask=mask)
    contours, cnts_bool = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    speed = 0
    acceleration = 0
    if contours:
        c = max(contours, key=cv.contourArea)
        if cv.contourArea(c) > 500:
            cv.drawContours(frame, [c], -1, (255, 0, 0), 2)
            M = cv.moments(c)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                if not first_frame:
                    distance = np.sqrt((cX - prev_cX) ** 2 + (cY - prev_cY) ** 2)  # ------> sqrt((x2-x1)^2+(y2-y1)^2)
                    speed = distance
                else:
                    speed = 0
                    first_frame = False
                if not first_frame:
                    acceleration = speed - prev_speed
                else:
                    acceleration = 0
                if not first_frame:
                    dx = cX - prev_cX
                    dy = cY - prev_cY
                prev_cX, prev_cY = cX, cY
                prev_speed = speed
                if speed <= 20:
                    color = (0, 255, 0)  # Slow (green)
                elif 20 < speed <= 50:
                    color = (0, 150, 255)  # Medium (orange)
                else:
                    color = (0, 0, 255)  # Fast (red)
                trajectory.append([frame_count,cX,cY,speed,acceleration,color[0],color[1],color[2],])
                append_to_file([frame_count, cX, cY, speed, acceleration])
    if len(trajectory) > 1:
        for i in range(1, len(trajectory)):
            pt1 = (trajectory[i - 1][1], trajectory[i - 1][2])
            pt2 = (trajectory[i][1], trajectory[i][2])
            color = (trajectory[i][5], trajectory[i][6], trajectory[i][7])

            # Trajectory (Frame)
            cv.line(frame, pt1, pt2, color, 2)
            cv.circle(frame, pt2, 5, color, -1)

    combined(frame, res_msk)
    frame_count += 1
    kay = cv.waitKey(20)
    if kay == 27:
        break
cap.release()
cv.destroyAllWindows()
show_plot(trajectory)
