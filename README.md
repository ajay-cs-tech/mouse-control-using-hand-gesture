# Hand Gesture Mouse Control

This project implements a virtual mouse control system using hand gestures captured through a webcam. It allows users to move the mouse cursor and perform clicks using their hand movements.

## Features

- Move the mouse cursor by moving your index finger
- Perform a click by bringing your thumb and index finger close together
- Real-time hand tracking and visualization

## Requirements

- Python 3.11 or later (latest version recommended)
- OpenCV (cv2)
- MediaPipe
- PyAutoGUI

## Installation

1. Clone this repository
2. Ensure you have the latest version of Python installed
3. Install the required packages:
   ```
   pip install opencv-python mediapipe pyautogui
   ```

## Usage

Run the script:
```
python main.py
```

- Use your index finger to move the cursor
- Bring your thumb and index finger together to click
- Press 'q' to quit the application

## Note

Ensure you have a working webcam and proper lighting for best results.
