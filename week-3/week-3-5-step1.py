import sys
import subprocess

print(sys.argv)
print(len(sys.argv))
subprocess.call(["python", "-h"])
