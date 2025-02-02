import shutil
import os

DIR = "2025-round1"

def newtemplate(source, destdir, name):
    os.makedirs(destdir, exist_ok=True)

    destpath = os.path.join(destdir, name)

    shutil.copy(source, destpath)
    print(f"file {source} copied to {destpath}")

try:
    name = input("input file name: ").lower().strip()
    if name == "quit":
        raise KeyboardInterrupt("")
    elif name.endswith(".py"):
        newtemplate("template.py", DIR, name)
    else:
        newtemplate("template.py", DIR, f"{name}.py")

except KeyboardInterrupt:
    print("exiting...")
