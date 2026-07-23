<div align="center">

# 🚀 Motion Tracking & Analytics System

<img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
<img src="https://img.shields.io/badge/OpenCV-Latest-green.svg" alt="OpenCV">
<img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">

<p align="center">
  <strong>An advanced real-time computer vision system for object tracking and movement analysis.</strong>
</p>

---

<p align="center">
  <img src="https://capsule-render.vercel.app/render?type=waving&color=auto&height=200&section=header&text=Motion%20Analytics&fontSize=70" />
</p>

</div>

## 📝 Project Overview

This project implements a robust motion tracking system using **Python** and **OpenCV**. It goes beyond simple tracking by converting raw pixel movements into meaningful physical metrics. The system utilizes color-based segmentation (HSV) to identify objects and mathematical models to analyze their behavior.

## ✨ Key Features

<table width="100%">
  <tr>
    <td width="50%">
      <h3>🔍 Precise Tracking</h3>
      <ul>
        <li>HSV-based color thresholding</li>
        <li>Contour detection algorithms</li>
        <li>Real-time Centroid calculation</li>
      </ul>
    </td>
    <td width="50%">
      <h3>📊 Data Analytics</h3>
      <ul>
        <li>Automatic trajectory logging (.csv)</li>
        <li>Velocity & Speed profiling</li>
        <li>3D Spatio-temporal visualization</li>
      </ul>
    </td>
  </tr>
</table>

---

## 🛠️ Technical Stack

| Component | Technology |
| :--- | :--- |
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) |
| **Computer Vision** | ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white) |
| **Math & Analysis** | `NumPy`, `SciPy` |
| **Visualization** | `Matplotlib` |

---

## 📈 Visual Analysis Results

The system automatically generates high-fidelity diagnostic plots. Below are the generated analytics:

<table align="center">
  <tr>
    <td align="center">
      <img src="analysis/chart-analysis.png" width="300"><br>
      <b>Speed Profile</b>
    </td>
    <td align="center">
      <img src="analysis/trajectory_3d.png" width="300"><br>
      <b>3D Trajectory</b>
    </td>
    <td align="center">
      <img src="analysis/movement-tracking.png" width="300"><br>
      <b>Movement Path</b>
    </td>
  </tr>
</table>

---

## 📂 Data Logs

In addition to visual plots, the system exports a structured `trajectory.csv` file:

| Column | Description |
| :--- | :--- |
| `frame` | The timestamp/frame number |
| `x_pos` | Horizontal coordinate |
| `y_pos` | Vertical coordinate |
| `speed` | Calculated instantaneous velocity |

---

---

## 🚀 Getting Started

Follow these step to set up the environment and run the motion tracking system on your local machine.

### 1️⃣ Prerequisites
Ensure you have **Python 3.8+** installed on your system. You can check your version by running:
```bash
python --version
git clone https://github.com/yourusername/motion-tracking-system.git
cd motion-tracking-system
pip install opencv-python numpy matplotlib
> python -m venv venv
> source venv/bin/activate  # On Windows use: venv\Scripts\activate
> pip install opencv-python numpy matplotlib scipy
