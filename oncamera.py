import cv2
import tkinter as tk
from tkinter import messagebox
import threading

class CameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Camera Control")

        # Button to start the camera
        self.start_button = tk.Button(root, text="Start Camera", command=self.start_camera)
        self.start_button.pack(pady=10)

        # Button to turn off the camera
        self.stop_button = tk.Button(root, text="Turn Off Camera", command=self.stop_camera, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        # Initialize camera and thread variables
        self.camera = None
        self.camera_running = False
        self.camera_thread = None

    def start_camera(self):
        if self.camera_running:
            messagebox.showinfo("Info", "Camera is already running.")
            return

        # Open the camera
        self.camera = cv2.VideoCapture(0)

        if not self.camera.isOpened():
            messagebox.showerror("Error", "Could not open camera.")
            return

        self.camera_running = True
        self.stop_button.config(state=tk.NORMAL)  # Enable the stop button

        # Start the camera feed in a separate thread
        self.camera_thread = threading.Thread(target=self.run_camera)
        self.camera_thread.start()

    def stop_camera(self):
        if not self.camera_running:
            messagebox.showinfo("Info", "Camera is not running.")
            return

        # Stop the camera
        self.camera_running = False

        if self.camera is not None:
            self.camera.release()
            self.camera = None

        cv2.destroyAllWindows()
        self.stop_button.config(state=tk.DISABLED)  # Disable the stop button
        messagebox.showinfo("Info", "Camera turned off.")

    def run_camera(self):
        while self.camera_running:
            ret, frame = self.camera.read()
            if not ret:
                messagebox.showerror("Error", "Failed to grab frame.")
                self.camera_running = False
                break

            cv2.imshow("Camera", frame)

            # Check if the user closes the camera window or presses 'q'
            key = cv2.waitKey(1)
            if key == ord('q'):
                self.stop_camera()
                break

        # Ensure camera and windows are closed after the loop
        if self.camera_running:
            self.camera.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root)
    root.mainloop()
