import shutil
import os
import sys

DIR = "2025-round2"

try:
    filename = sys.argv[1]
except:
    filename = ""

def newtemplate(source, destdir, name):
    os.makedirs(destdir, exist_ok=True)
    destpath = os.path.join(destdir, name)

    if os.path.exists(destpath):
        print(f"file {destpath} already exists. quitting")
        sys.exit(1)

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
