import subprocess
import os
import signal

def start_recording(output_path="videos/test_run.mp4"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    return subprocess.Popen([
        'ffmpeg', '-y',
        '-f', 'gdigrab',             # Use 'x11grab' on Linux
        '-framerate', '15',
        '-i', 'desktop',
        '-video_size', '1920x1080',
        output_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def stop_recording(process):
    process.send_signal(signal.CTRL_C_EVENT if os.name == 'nt' else signal.SIGINT)
