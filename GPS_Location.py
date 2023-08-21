import sys
import os
import platform
import tkinter as tk
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from prettytable import PrettyTable

def get_downloads_directory():
    system_platform = platform.system()
    if system_platform == "Windows":
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    elif system_platform == "Linux":
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    else:
        return os.getcwd()  # default to current directory for other platforms

def save_to_txt(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def get_exif_data(img):
    # ... (same as before)

print("\nExtract Image Properties and EXIF Data\n")
image_path = open_file_dialog()

if not image_path:
    sys.exit("\nNo file selected\n")

try:
    with Image.open(image_path) as img:
        # ... (same as before)

        # Automatically save to Downloads directory
        downloads_dir = get_downloads_directory()
        filename = os.path.join(downloads_dir, "image_metadata.txt")
        save_to_txt(filename, str(tbl))
        print(f"\nData saved to {filename}")

except Exception as err:
    sys.exit(f"\nException: {err}")
