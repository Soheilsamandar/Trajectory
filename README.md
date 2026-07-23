<div align="center">

# 🚀 Motion Trackin & Analytics System

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

This project implement a robust motion tracking system using **Python** and **OpenCV**. It goes beyond simple tracking by converting raw pixel movements into meaningful physical metrics. The system utilizes color-based segmentation (HSV) to identify objects and mathematical models to analyze their behavior.

## ✨ Key Features

<table width="100%">
  <tr>
    <td width="50%">
      <h3>🔍 Precise Tracking</h3
      <ul>
        <li>HSV-based color thresholding</li>
        <li>Contour detection algorithms</li>
        <li>Real-time Centroid calculation</li>
      </ul>
    </td>
    <td width="50%">
      <h3>📊 Data Analytics</h3
      <ul>
        <li>Automatic trajectory logging (.csv)</li>
        <li>Velocity & Speed profiling</li>
        <li>3D Spatio-temporal visualization</li>
      </ul>
    </td>
  </tr>
</table>

---

## 🛠️ Technical Stac

| Component | Technology |
| :--- | :--- |
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) |
| **Computer Vision** | ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white) |
| **Math & Analysis** | `NumPy`, `SciPy` |
| **Visualization** | `Matplotlib` |

---

## 📈 Analysis Output

The system automatically generates an `analysis/` directory containing:

1.  **`chart-analysis.png`**: A dual-axis plot showing the velocity profile of the object over time.
2.  **`trajectory_3d.png`**: A 3D representation of the object's path, mapping $X$, $Y$, and $Time$ (Frames).
3.  **`trajectory.csv`**: A structured data log containing:
    *   `Frame Number`
    *   `X-Coordinate`
    *   `Y-Coordinate`
    *   `Speed (px/f)`

---

## 🚀 Gettin Started

### Prerequisites
```bash
pip install opencv-python numpy matplotlib scipy
