import pyautogui  # For simulating keyboard presses

def volumeup():
    """
    Simulates pressing the volume up key multiple times to increase system volume.
    """
    for _ in range(5):  # Adjust the range for desired volume increase
        pyautogui.press("u")

def volumedown():
    """
    Simulates pressing the volume down key multiple times to decrease system volume.
    """
    for _ in range(5):  # Adjust the range for desired volume decrease
        pyautogui.press("d")
