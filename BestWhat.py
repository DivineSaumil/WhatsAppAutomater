import pyautogui
import subprocess

phone_numbers = [""]

message = "Hello, this is a test message, testing the WhatsApp code."

image_path = r'C:\Users\Ajay Kumar\Desktop\Python\.venv\Scripts\Image'  # Replace with the path to your image file

time.sleep(5)
# Open Windows Explorer to copy image
subprocess.Popen(['explorer', image_path])

time.sleep(3)
# Select the Images
pyautogui.hotkey("ctrl", "a")
time.sleep(2)
# Copy the Images
pyautogui.hotkey("ctrl", "c")
time.sleep(2)

# Replace this with the actual path to the WhatsApp shortcut on your desktop
shortcut_path = r'C:\Users\Ajay Kumar\Desktop\WhatsApp - Shortcut.lnk'

try:
    # Open WhatsApp Desktop Application (Ensure full screen)
    subprocess.Popen([shortcut_path], shell=True)
except FileNotFoundError:
    print("Shortcut not found or could not be opened.")

time.sleep(1)

for phone_numbers in phone_numbers:
    # Search
    pyautogui.hotkey("ctrl", "f")
    time.sleep(1)
    pyautogui.write(phone_numbers)
    time.sleep(2)
    # Select the recipient
    pyautogui.click(325, 281)
    time.sleep(1)
    # Paste the images
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    # Write the caption
    pyautogui.write(message)
    time.sleep(1)
    # Send
    pyautogui.press("Enter")
    time.sleep(5)
