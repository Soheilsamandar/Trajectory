import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt
import csv
output_dir = "analysis"
FILE_NAME = os.path.join(output_dir, "trajectory.csv")
def resize(frame,perc=40):
    width = int(frame.shape[1] *perc /100)
    height=int(frame.shape[0] *perc /100)
    dim = (width,height)
    res =cv.resize(frame,dim,interpolation=cv.INTER_AREA)
    return res

def create_mask(frame,low,up):
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv,low,up)
    kernel = np.ones((5,5),np.uint8)
    mask = cv.morphologyEx(mask,cv.MORPH_OPEN,kernel)
    return mask

def combined(frame,mask):
    web = resize(frame)
    res = resize(mask)
    if len(res.shape) == 2:
        res = cv.cvtColor(res, cv.COLOR_GRAY2BGR)
    h, w = web.shape[:2]
    res = cv.resize(res, (w, h))
    combined = np.hstack((web, res))
    cv.imshow("webcam | result", combined)

def remove_file(file_name):
    if os.path.isfile(file_name):
        os.remove(file_name)

def append_to_file(data):
    with open(FILE_NAME, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def show_plot(trajectory, show=False):
    output_dir = 'analysis'
    os.makedirs(output_dir, exist_ok=True) 
    if len(trajectory) > 1:
        
        frames = np.array([item[0] for item in trajectory])
        x_coords = np.array([item[1] for item in trajectory])
        y_coords = np.array([item[2] for item in trajectory])
        speeds = np.array([item[3] for item in trajectory])
        accelerations = np.array([item[4] for item in trajectory])

        start_x, start_y = x_coords[0], y_coords[0]
        displacements = np.sqrt((x_coords - start_x)**2 + (y_coords - start_y)**2)


        def smooth(data, window=5):
            if len(data) < window: return data
            return np.convolve(data, np.ones(window)/window, mode='same')

        smooth_accel = smooth(accelerations, window=5)
        smooth_speed = smooth(speeds, window=5)
        fig = plt.figure(figsize=(14, 12))
        # 1. Speed , Acceleration , Displacement
        plt.subplot(3, 1, 1)
        plt.plot(frames, smooth_speed, 'b-', linewidth=2, label='Speed')
        plt.fill_between(frames, smooth_speed, color='blue', alpha=0.1) 
        plt.title('Speed Analysis')
        plt.ylabel('Speed (px/frame)')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()

        plt.subplot(3, 1, 2)
        plt.plot(frames, smooth_accel, 'r-', linewidth=2, label='Acceleration')
        plt.fill_between(frames, smooth_accel, color='red', alpha=0.1)
        plt.title('Acceleration Analysis')
        plt.ylabel('Accel (px/frame²)')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()

        
        plt.subplot(3, 1, 3)
        plt.plot(frames, displacements, 'g-', linewidth=2, label='Total Displacement')
        plt.fill_between(frames, displacements, color='green', alpha=0.1)
        plt.title('Cumulative Displacement from Start')
        plt.xlabel('Frame')
        plt.ylabel('Distance (px)')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'chart-analysis.png'))
        
        # 2. Movement Trajectory 
        plt.figure(figsize=(10, 6))
        plt.plot(x_coords, y_coords, marker='', linestyle='-', color='blue', alpha=0.6)
        plt.scatter(x_coords[0], y_coords[0], color='green', s=100, label='Start', zorder=5)
        plt.scatter(x_coords[-1], y_coords[-1], color='red', s=100, label='End', zorder=5)
        plt.title('Object Path Trajectory')
        plt.gca().invert_yaxis() 
        plt.xlabel('X Position (px)')
        plt.ylabel('Y Position (px)')
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.legend()
        plt.savefig(os.path.join(output_dir, 'movement_object.png'))
        
        # 3. 3D Trajectory
        fig_3d = plt.figure(figsize=(10, 8))
        ax_3d = fig_3d.add_subplot(111, projection='3d')
        ax_3d.plot(x_coords, y_coords, frames, marker='', linestyle='-', color='blue', alpha=0.6)
        ax_3d.set_title('3D Spatio-Temporal Trajectory')
        ax_3d.set_xlabel('X (px)')
        ax_3d.set_ylabel('Y (px)')
        ax_3d.set_zlabel('Frame (Time)')
        ax_3d.invert_yaxis()
        plt.savefig(os.path.join(output_dir, 'trajectory_3d.png'))
                
        if show:
            print("Displaying plots...")
            plt.show() 
    else:
        print("No trajectory data was collected.")
