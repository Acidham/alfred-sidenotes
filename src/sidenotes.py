#!/usr/bin/python3

from subprocess import PIPE, Popen

from Alfred3 import Items, Tools

scpt = """
tell application "SideNotes"

	set folders_object to folders
	set folder_list to {}
	repeat with f in folders_object
		set folder_list to folder_list & name of item 1 of f
	end repeat
end tell

return folder_list
"""


def get_folders(folders_string: str) -> list:
    f = [x.strip("\n") for x in folders_string.split(",")]
    return [x.strip() for x in f]


query = Tools.getArgv(1)

p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
stdout, stderr = p.communicate(scpt)
folders = get_folders(stdout)

wf = Items()

for f in folders:
    if query == "" or query in f:
        wf.setItem(
            title=f,
            subtitle=f"Add note to Folder \"{f}\"",
            arg=f
        )
        wf.addItem()

wf.write()
