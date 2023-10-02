import pyautogui
import imageio


def record_screen(screen_recording):
    screen_size = pyautogui.size()

    # List to store video frames
    frames = []

    # Recording active flag
    # noinspection PyGlobalUndefined
    global recording_active
    recording_active: bool = True

    # Start recording
    while recording_active:
        frames.append(pyautogui.screenshot(region=(0,0, screen_size[0], screen_size[1])))

    # Save frames as video file
    imageio.mimsave(screen_recording, frames, format='mp4')

    # Save recording to db

    print('Screen recording has been saved as:', screen_recording)