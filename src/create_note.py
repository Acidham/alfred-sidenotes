#!/usr/bin/python3

import sys
from subprocess import PIPE, Popen

from Alfred3 import Tools

note = Tools.getArgv(1)
target_folder = Tools.getEnv("target_folder")

scpt = f"""
tell application "SideNotes"
	set n to make new note at folder "{target_folder}"
	set text of n to "{note}"
end tell
"""
p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
stdout, stderr = p.communicate(scpt)

sys.stdout.write(stderr)
