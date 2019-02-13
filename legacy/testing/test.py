import subprocess
import time

subprocess.Popen(["paplay", "test1.ogg"])
time.sleep(0.5)
subprocess.Popen(["paplay", "test2.ogg"])