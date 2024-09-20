import subprocess
import os

def install_requirements():
    requirements_file = 'requirements.txt'
    if os.path.exists(requirements_file):
        try:
            subprocess.check_call(['pip', 'install', '-r', requirements_file])
        except subprocess.CalledProcessError as e:
            print(f"Failed to install requirements: {e}")
        else:
            print("Requirements installed successfully.")
    else:
        print(f"{requirements_file} not found.")
