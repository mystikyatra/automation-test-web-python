import subprocess
import os
import signal
import platform

def start_recording(output_path="videos/test_run.mp4"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Windows uses gdigrab; Linux would use x11grab (but we skip that here)
    cmd = [
        "ffmpeg", "-y",
        "-f", "gdigrab",
        "-framerate", "15",
        "-i", "desktop",
        "-video_size", "1920x1080",
        output_path
    ]

    return subprocess.Popen(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP  # For clean SIGINT
    )

def stop_recording(process):
    if platform.system() == "Windows":
        process.send_signal(signal.CTRL_BREAK_EVENT)  # Use CTRL_BREAK_EVENT for subprocess on Windows
    else:
        process.send_signal(signal.SIGINT)
