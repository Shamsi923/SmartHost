import os
import platform
import shutil
from datetime import datetime

print("=" * 40)
print("       SMARTHOST SERVER MONITOR")
print("=" * 40)

print("Hostname:", platform.node())
print("Operating System:", platform.system())
print("Date:", datetime.now())

print("\nDISK INFORMATION")
disk = shutil.disk_usage("/")
print("Total:", round(disk.total / (1024**3), 2), "GB")
print("Used:", round(disk.used / (1024**3), 2), "GB")
print("Free:", round(disk.free / (1024**3), 2), "GB")

print("\nMEMORY INFORMATION")
with open("/proc/meminfo") as f:
    for line in f:
        if line.startswith(("MemTotal", "MemAvailable")):
            print(line.strip())

print("\nSERVER STATUS: RUNNING")
print("=" * 40)
