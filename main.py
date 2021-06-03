import datetime
from PIL import ImageGrab
import numpy as np
import cv2
from pyautogui import size


def activate_webcam():
    return True if input('Would you like to activate Webcam? (y / n): ') == 'y' else False


def main():
    width, height = size()

    time_stamp = datetime.datetime.now().strftime('%d-%m-%y - %H-%M-%S')

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    capture_video = cv2.VideoWriter(f'{time_stamp}.mp4', fourcc, 20.0, (width, height))

    activate_the_webcam = activate_webcam()
    if activate_the_webcam:
        webcam = cv2.VideoCapture(0)

    while True:
        img = ImageGrab.grab(bbox=(0, 0, width, height))
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        if activate_the_webcam:
            _, frame = webcam.read()
            frame = cv2.resize(frame, (200, 150), interpolation=cv2.INTER_AREA)
            fr_height, fr_width, _ = frame.shape
            img_final[0: fr_height, 0: fr_width, :] = frame[0: fr_height, 0: fr_width, :]

        cv2.imshow('My Screen', img_final)
        capture_video.write(img_final)
        if cv2.waitKey(10) == ord('q'):
            break


if __name__ == '__main__':
    main()
