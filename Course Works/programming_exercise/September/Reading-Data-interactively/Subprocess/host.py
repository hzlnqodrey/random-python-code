#!/usr/bin/env python3

import subprocess

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)

print(result.returncode)
print(result.stdout.decode().split()) # output of the host command

result = subprocess.run(["rm", "will_delete.py"], capture_output=True)
print(result.returncode)

print(result.stdout)
print(result.stderr)
print(result.stderr.decode())
