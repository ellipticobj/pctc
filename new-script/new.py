import shutil
import os
import sys

DIR = "2025-round1"

filename = sys.argv[1]

def newtemplate(source, destdir, name):
    os.makedirs(destdir, exist_ok=True)

    destpath = os.path.join(destdir, name)

    shutil.copy(source, destpath)
    print(f"file {source} copied to {destpath}")

try:
    if filename:
        name = filename.strip().lower()
    else:
        name = input("input file name: ").lower().strip()

    if name == "quit":
        raise KeyboardInterrupt("")
    elif name.endswith(".py"):
        newtemplate("template.py", DIR, name)
    else:
        newtemplate("template.py", DIR, f"{name}.py")

except KeyboardInterrupt:
    print("exiting...")
