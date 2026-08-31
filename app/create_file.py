import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-d", nargs="+")
parser.add_argument("-f", nargs="?")
args = parser.parse_args()
print(args.d, args.f)

file_path = ""
if args.d:
    os.makedirs("/".join(args.d), exist_ok=True)
    file_path += "/".join(args.d) + "/"

if args.f:
    file_path += args.f
    with open(file_path, "a") as file:
        if os.path.getsize(file_path) != 0:
            file.write("\n")
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        count = 1
        while True:

            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{count} {line}\n")
            count += 1
